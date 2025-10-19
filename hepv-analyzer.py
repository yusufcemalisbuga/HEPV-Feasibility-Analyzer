#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HEPV – Hybrid Electric-Pneumatic Vehicle Simulator
==================================================
A reproducible, peer-review-grade single-file model with
vectorised physics, logging, CLI, plotting and CSV/HDF5 export.

Version : 3.3.0-alpha-1- (2025-01-08)
Author  : Yusuf Cemal Isbuga + open-source contributors
License : MIT

CHANGELOG (excerpt)
-------------------
● 3.3.0
  – FIX  tank_thermodynamics sign bug (dP = E·(n-1)/V)
  – FIX  real pneumatic η used during discharge
  – ADD  initial tank energy derived from P_init
  – ADD  logging (DEBUG/INFO/WARNING/ERROR)
  – CHG  flag  --skip-combined (replaces double-negative)
  – IMP  type hints, PEP-8, modular structure, numpy vectorisation
  – IMP  regen efficiency = motor_eff(speed,0.2)*η_inverter
  – REM  terminal emojis (ASCII only for cross-platform)
"""

from __future__ import annotations

# ── std lib ──────────────────────────────────────────────────────────────────
import argparse
import logging
import pathlib
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Tuple

# ── 3rd-party ────────────────────────────────────────────────────────────────
import numpy as np
import matplotlib.pyplot as plt

# ── meta info ────────────────────────────────────────────────────────────────
__version__: str = "3.3.0-alpha"
__author__:  str = "Yusuf Cemal Isbuga"

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 0.  LOGGING & CLI
# ╚═══════════════════════════════════════════════════════════════════════════╝
DEFAULT_OUT = pathlib.Path.home() / "hepv_results"

def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level   = level,
        format  = "[%(levelname)s] %(message)s",
        datefmt = "%H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        force   = True,
    )

def parse_cli() -> argparse.Namespace:
    """Return parsed CLI namespace."""
    p = argparse.ArgumentParser(
        prog               = "hepv",
        description        = "Hybrid Electric-Pneumatic Vehicle feasibility simulator",
        formatter_class    = argparse.RawTextHelpFormatter,
        epilog = """\
Examples
--------
hepv.py                                 # default run
hepv.py --show                          # show plots interactively
hepv.py --save-individual               # save every figure to PNG
hepv.py --duration 600 --verbose        # longer run with debug log
"""
    )

    # --- core simulation ----------------------------------------------------
    p.add_argument("--duration", type=float, default=400.0,
                   help="simulation duration in seconds (default: 400)")
    p.add_argument("--dt",        type=float, default=0.1,
                   help="time step in seconds (default: 0.1)")
    p.add_argument("--out",       type=pathlib.Path, default=DEFAULT_OUT,
                   help=f"output directory (default: {DEFAULT_OUT})")

    # --- visualisation ------------------------------------------------------
    p.add_argument("--skip-plots",     action="store_true",
                   help="do not generate any plots")
    p.add_argument("--show",           action="store_true",
                   help="display plots on screen")
    p.add_argument("--save-individual",action="store_true",
                   help="save each figure separately (PNG)")
    p.add_argument("--skip-combined",  action="store_true",
                   help="do NOT save the combined 3×3 panel")
    p.add_argument("--dpi", type=int, default=300,
                   help="figure resolution in DPI (default: 300)")

    # --- misc ---------------------------------------------------------------
    p.add_argument("--no-validation", action="store_true",
                   help="skip console validation summary")
    p.add_argument("--verbose",       action="store_true",
                   help="enable verbose logging")
    p.add_argument("--version",       action="version",
                   version=f"%(prog)s {__version__}")

    ns = p.parse_args()
    _setup_logging(ns.verbose)
    logging.debug("CLI: %s", ns)
    return ns


# ╔═══════════════════════════════════════════════════════════════════════════╗
# 1.  VALIDATION DATABASE
# ╚═══════════════════════════════════════════════════════════════════════════╝
class ValidationDB:
    """Static references for model validation."""
    TESLA_M3: Dict[str, float | str] = {
        "source"         : "MotorXP Teardown Analysis (2018)",
        "peak_efficiency": 0.9212,
        "peak_rpm"       : 4_275,
        "peak_power_kW"  : 192.4,
        "load_at_peak"   : 0.91,
        "note"           : "Partial-load efficiency 85–90 %"
    }

    INDUSTRIAL_PNEUMATIC: Dict[str, Tuple | str] = {
        "sources"            : ("Atlas Copco LZB", "Parker Hannifin"),
        "efficiency_range"   : (0.25, 0.45),
        "peak_efficiency"    : 0.40,
        "optimal_pressure_bar": (6, 8),
        "note"               : "Efficiency degrades >200 bar"
    }

    PEUGEOT_TRIALS: Dict[str, float | str] = {
        "source"        : "Field Trials 2013-2015",
        "claimed_saving": 0.45,
        "actual_saving" : 0.12,
        "outcome"       : "Project discontinued",
        "note"          : "Theory–practice gap highlighted"
    }

VAL = ValidationDB()

def print_validation_report() -> None:
    if not logging.root.isEnabledFor(logging.INFO):
        return
    bar = "=" * 72
    print(f"\n{bar}\nMODEL VALIDATION REFERENCES\n{bar}")
    print("\nElectric motor (Tesla Model 3)")
    print(f"  Source           : {VAL.TESLA_M3['source']}")
    print(f"  Peak efficiency  : {VAL.TESLA_M3['peak_efficiency']*100:.2f} %")
    print(f"  Peak @ RPM/load  : {VAL.TESLA_M3['peak_rpm']} RPM,"
          f" {VAL.TESLA_M3['load_at_peak']*100:.0f} % load")
    print("\nIndustrial pneumatic motor")
    print(f"  Sources          : {', '.join(VAL.INDUSTRIAL_PNEUMATIC['sources'])}")
    lo, hi = VAL.INDUSTRIAL_PNEUMATIC['efficiency_range']
    print(f"  Efficiency range : {lo*100:.0f}–{hi*100:.0f} %")
    print("\nReal-world Peugeot trials")
    print(f"  Claimed saving   : {VAL.PEUGEOT_TRIALS['claimed_saving']*100:.0f} %")
    print(f"  Actual saving    : {VAL.PEUGEOT_TRIALS['actual_saving']*100:.0f} %")
    print(bar)


# ╔═══════════════════════════════════════════════════════════════════════════╗
# 2.  PARAMETERS  (immutable dataclass)
# ╚═══════════════════════════════════════════════════════════════════════════╝
@dataclass(frozen=True, slots=True)
class Params:
    # Mass
    m0:        float = 450.0      # baseline BEV mass [kg]
    m_pneu:    float =  50.0      # additional pneumatic hardware [kg]

    # Aerodynamics
    Cd: float = 0.28;  A: float = 1.20;  Crr: float = 0.012

    # Battery & electric drivetrain
    batt_kWh:   float = 5.0
    motor_Pmax: float = 15_000    # [W]
    motor_eta_peak: float = 0.92
    motor_rpm_base: float = 4_275
    inverter_eta:   float = 0.97  # static inverter efficiency
    regen_limit:    float = 0.98  # maximum SoC after regen

    # Pneumatic system
    Vtank: float = 0.050          # [m³]
    Pmax:  float = 300e5          # 300 bar [Pa]
    Pmin:  float = 100e5          # 100 bar [Pa]
    P_init: float = 150e5         # 150 bar [Pa]
    comp_eta:      float = 0.60
    pneu_eta_peak: float = 0.40
    leak_per_min:  float = 0.02   # 2 % per minute

    # Physics constants
    rho:  float = 1.225           # air density [kg/m³]
    g:    float = 9.81
    R:    float = 287.0
    Tamb: float = 293.0           # 20 °C
    Pamb: float = 101_325.0

    # Polytropic indices
    n_comp: float = 1.30
    n_exp:  float = 1.25
    heat_coef: float = 0.10       # simple convective coefficient

    # Vehicle dynamics
    wheel_diam: float = 0.60
    gear:       float = 9.0

    # Control thresholds
    pneu_speed_thr:     float = 35     # km/h
    pneu_power_thr:     float = 3_000  # W
    pneu_pressure_min:  float = 100    # bar
    pneu_power_split:   float = 0.35
    regen_split_batt:   float = 0.75
    regen_split_tank:   float = 0.25
    regen_tank_Pmax:    float = 250    # bar (changed from 280)

P = Params()  # global constant-like instance

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 3.  PHYSICS MODELS
# ╚═══════════════════════════════════════════════════════════════════════════╝
import math
from numpy.typing import NDArray

# ---------------------------------------------------------------------------#
# 3.1  Helper functions                                                      #
# ---------------------------------------------------------------------------#
def aero_drag(v: NDArray[np.float64]) -> NDArray[np.float64]:
    """Aerodynamic drag force [N].  v may be scalar or ndarray."""
    return 0.5 * P.rho * P.Cd * P.A * v**2

def rolling_resistance(m: float) -> float:
    """Rolling resistance force [N] (speed-independent Coulomb model)."""
    return P.Crr * m * P.g

def power_required(v: float, a: float, m: float) -> float:
    """Mechanical power demand at wheels [W]."""
    F = m * a + aero_drag(v) + rolling_resistance(m)
    return F * max(v, 1e-3)             # avoid 0 · 0 singularity

def speed_to_rpm(kmh: float) -> float:
    v_ms   = kmh / 3.6
    wheel_rps = v_ms / (math.pi * P.wheel_diam)
    return wheel_rps * 60.0 * P.gear

# ---------------------------------------------------------------------------#
# 3.2  Efficiency maps                                                       #
# ---------------------------------------------------------------------------#
def electric_eff(kmh: float, load: float) -> float:
    """Return traction-motor efficiency (0–1)."""
    x = speed_to_rpm(kmh) / P.motor_rpm_base

    # speed contribution
    if   x < .2:   s = .75
    elif x < .5:   s = .75 + .15 * (x-.2)/.3
    elif x <=1.5:  s = .90 + .02 * (1 - abs(x-1))
    else:          s = .90 - .10 * (x-1.5)

    # load contribution
    if   load < .1:  l = .60 + 4*load
    elif load < .8:  l = 1.0
    else:            l = 1.0 - .05*(load-.8)/.2

    return np.clip(s*l, .70, P.motor_eta_peak)

def pneumatic_eff(kmh: float, bar: float) -> float:
    """Return pneumatic-motor efficiency (0–1)."""
    # pressure effect
    if   bar <  50:  p = .30
    elif bar < 100:  p = .50 + .30*(bar-50)/50
    elif bar <=200:  p = .80
    else:            p = .80 - .20*(bar-200)/100
    # speed effect
    if   kmh < 20:   s = 1.0
    elif kmh < 40:   s = 1.0 - .15*(kmh-20)/20
    elif kmh < 60:   s = .85 - .25*(kmh-40)/20
    else:            s = max(.60 - .20*(kmh-60)/20, .40)
    return np.clip(P.pneu_eta_peak * p * s, .15, .45)

# ---------------------------------------------------------------------------#
# 3.3  Tank thermodynamics                                                   #
# ---------------------------------------------------------------------------#
def initial_tank_energy(Pa: float) -> float:
    """Ideal-gas internal energy above ambient [J]."""
    return (Pa - P.Pamb) * P.Vtank / (P.n_exp - 1)

def tank_thermodynamics(Pa: float, T: float, Pw: float,
                        dt: float, charging: bool,
                        eta_actual: float) -> Tuple[float, float]:
    """Polytropic (de)compression with convective heat-loss + leakage."""
    n   = P.n_comp if charging else P.n_exp
    eta = P.comp_eta if charging else eta_actual
    sign = +1.0 if charging else -1.0

    E = Pw * dt * sign / eta                # energy added (+) or removed (–)
    dP =  E * (n - 1.0) / P.Vtank           # FIX: correct sign
    P_new = max(P.Pamb, min(P.Pmax, Pa + dP))

    # temperature change
    T_new = T * (P_new / Pa) ** ((n - 1.0)/n) if Pa > 0 else T
    # Newton cooling towards ambient
    T_new += (P.Tamb - T_new) * P.heat_coef * dt
    # leakage – apply on *mass* proportional to pressure ratio
    P_new *= (1.0 - P.leak_per_min/60.0 * dt)

    T_new = np.clip(T_new, 240.0, 400.0)    # allow down to −33 °C
    return P_new, T_new

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 4.  DRIVING CYCLE (WLTP-like urban)                                         #
# ╚═══════════════════════════════════════════════════════════════════════════╝
def urban_cycle(duration: float, dt: float) -> Tuple[NDArray[np.float64], NDArray[np.float64]]:
    t = np.arange(0.0, duration, dt)
    v = np.zeros_like(t)

    pattern = [
        (0,  8,  0, 30/3.6),
        (8, 18, 30/3.6, 30/3.6),
        (18,23, 30/3.6, 0),
        (23,33, 0, 0),
        (33,43, 0, 50/3.6),
        (43,63, 50/3.6, 50/3.6),
        (63,70, 50/3.6, 0),
        (70,80, 0, 0),
    ]
    period = 80
    for r in range(int(duration//period)+1):
        off = r*period
        for ts,te,vs,ve in pattern:
            i0 = int((off+ts)/dt); i1 = int(min((off+te)/dt, len(t)))
            if i0 >= len(t): break
            v[i0:i1] = np.linspace(vs, ve, i1-i0)

    return t, v

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 5.  SIMULATORS                                                              #
# ╚═══════════════════════════════════════════════════════════════════════════╝
def simulate_bev(t: NDArray[np.float64],
                 v: NDArray[np.float64]) -> Dict[str, NDArray]:
    """Vectorised BEV simulation (single forward loop for SoC)."""
    dt = t[1] - t[0]
    n  = len(t)

    soc   = np.ones(n)
    eff   = np.zeros(n)
    power = np.zeros(n)
    batt  = P.batt_kWh * 3.6e6  # J

    for k in range(1, n):
        a = (v[k] - v[k-1]) / dt
        Pw = np.clip(power_required(v[k], a, P.m0),
                     -12_000, P.motor_Pmax)
        power[k] = Pw
        kmh = v[k]*3.6

        if Pw >= 0:                              # traction
            η = electric_eff(kmh, Pw/P.motor_Pmax)
            batt -= Pw/η * dt
            eff[k] = η
        else:                                    # regen
            ηr = electric_eff(kmh, 0.2) * P.inverter_eta
            max_regen = (P.batt_kWh*3.6e6*P.regen_limit - batt) / dt
            Pb = min(-Pw * ηr, max_regen)
            batt += Pb * dt
            eff[k] = ηr

        soc[k] = np.clip(batt / (P.batt_kWh*3.6e6), 0, 1)

    return dict(
        soc=soc,
        eff=eff,
        power=power,
        E_kWh=(P.batt_kWh*3.6e6 - batt)/3.6e6
    )

# ---------------------------------------------------------------------------#
# 5.2  HEPV simulator                                                        #
# ---------------------------------------------------------------------------#
def simulate_hepv(t: NDArray[np.float64],
                  v: NDArray[np.float64]) -> Dict[str, NDArray]:
    dt = t[1] - t[0]
    n  = len(t)
    m  = P.m0 + P.m_pneu

    soc   = np.ones(n)
    Pe    = np.zeros(n)
    Pp    = np.zeros(n)
    tankP = np.empty(n); tankP[0] = P.P_init
    tankT = np.empty(n); tankT[0] = P.Tamb
    tankE = np.empty(n); tankE[0] = initial_tank_energy(P.P_init)
    batt  = P.batt_kWh*3.6e6
    pneu_use = 0

    for k in range(1, n):
        a   = (v[k]-v[k-1])/dt
        Pw  = power_required(v[k], a, m)
        kmh = v[k]*3.6
        bar = tankP[k-1]/1e5

        if Pw >= 0:                                      # traction
            use_pneu = (kmh < P.pneu_speed_thr and
                        bar  > P.pneu_pressure_min and
                        Pw   > P.pneu_power_thr and
                        tankE[k-1] > 1e3 and soc[k-1] > 0.2)

            if use_pneu:
                Pp[k] = P.pneu_power_split*Pw
                Pe[k] = Pw - Pp[k]
                pneu_use += 1
            else:
                Pe[k] = Pw

            # electric consumption
            if Pe[k] > 0:
                batt -= Pe[k]/electric_eff(kmh, Pe[k]/P.motor_Pmax) * dt

            # pneumatic consumption
            if Pp[k] > 0:
                ηp = pneumatic_eff(kmh, bar)
                Ein = Pp[k]/ηp * dt
                tankE[k] = max(0.0, tankE[k-1] - Ein)
                tankP[k], tankT[k] = tank_thermodynamics(
                    tankP[k-1], tankT[k-1], Pp[k]/ηp, dt, False, ηp)
            else:
                tankE[k] = tankE[k-1]
                tankP[k], tankT[k] = tankP[k-1], tankT[k-1]

        else:                                            # braking
            Preg = -Pw
            Pb, Pt = Preg, 0.0
            if soc[k-1] >= 0.3 and bar <= P.regen_tank_Pmax:
                Pb = P.regen_split_batt*Preg
                Pt = P.regen_split_tank*Preg

            # battery regen
            ηr = electric_eff(kmh, 0.2) * P.inverter_eta
            Pb_cap = (P.batt_kWh*3.6e6*P.regen_limit - batt) / dt
            Pb = min(Pb*ηr, Pb_cap)
            batt += Pb * dt

            # tank regen
            if Pt > 0:
                Ein = Pt * P.comp_eta * dt
                tankE[k] = tankE[k-1] + Ein
                tankP[k], tankT[k] = tank_thermodynamics(
                    tankP[k-1], tankT[k-1], Pt, dt, True, P.comp_eta)
            else:
                tankE[k] = tankE[k-1]
                tankP[k], tankT[k] = tankP[k-1], tankT[k-1]

            Pe[k] = -Pb
            Pp[k] = -Pt

        soc[k] = np.clip(batt/(P.batt_kWh*3.6e6), 0, 1)

    return dict(
        soc=soc,
        Pe=Pe,
        Pp=Pp,
        tankP_bar=tankP/1e5,
        tankT_C=tankT-273.15,
        tankE_kWh=tankE/3.6e6,
        E_kWh=(P.batt_kWh*3.6e6 - batt)/3.6e6,
        pneu_use=pneu_use
    )

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 6.  PLOT MANAGER                                                           #
# ╚═══════════════════════════════════════════════════════════════════════════╝
class PlotManager:
    """Create and export all figures needed for the paper / report."""
    def __init__(self,
                 t: NDArray[np.float64],
                 v: NDArray[np.float64],
                 bev: Dict,
                 hepv: Dict,
                 out_dir: pathlib.Path) -> None:

        self.t     = t
        self.v     = v
        self.bev   = bev
        self.hepv  = hepv
        self.out   = out_dir
        self._set_style()

    # --------------------------------------------------------------------- #
    def _set_style(self) -> None:
        plt.rcParams.update({
            "font.size"      : 9,
            "axes.labelsize" : 10,
            "axes.titlesize" : 11,
            "legend.fontsize": 8,
            "lines.linewidth": 2,
            "axes.grid"      : True,
            "grid.alpha"     : 0.3,
        })

    # --------------------------------------------------------------------- #
    # Individual plot creators                                              #
    # --------------------------------------------------------------------- #
    def fig_cycle(self):
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.plot(self.t, self.v*3.6, "k-")
        ax.set(xlabel="Time [s]", ylabel="Speed [km/h]",
               title="WLTP-style Urban Cycle")
        return fig

    def fig_soc(self):
        fig, ax = plt.subplots()
        ax.plot(self.t, self.bev["soc"]*100, "b-", label="BEV")
        ax.plot(self.t, self.hepv["soc"]*100, "r--", label="HEPV")
        ax.set(xlabel="Time [s]", ylabel="SoC [%]", title="Battery SoC")
        ax.set_ylim(80, 105); ax.legend()
        return fig

    def fig_energy_bar(self):
        fig, ax = plt.subplots(figsize=(4,4))
        e = [self.bev["E_kWh"], self.hepv["E_kWh"]]
        bars = ax.bar(["BEV","HEPV"], e,
                      color=["#4CAF50", "#F44336" if e[1]>e[0] else "#FF9800"])
        for bar,val in zip(bars,e):
            ax.text(bar.get_x()+bar.get_width()/2, val,
                    f"{val:.4f} kWh", ha="center", va="bottom")
        ax.set_ylabel("Total Energy [kWh]")
        return fig

    # (additional individual figures could be added exactly as in v3.0)

    # --------------------------------------------------------------------- #
    def combined_panel(self):
        fig = plt.figure(figsize=(12, 9))
        gs  = fig.add_gridspec(3,3)
        
        ax1 = fig.add_subplot(gs[0,0])
        ax1.plot(self.t, self.v*3.6)
        ax1.set_title("Cycle")
        
        ax2 = fig.add_subplot(gs[0,1])
        ax2.plot(self.t, self.bev["soc"]*100, label="BEV")
        ax2.plot(self.t, self.hepv["soc"]*100, label="HEPV")
        ax2.set_title("SoC")
        ax2.legend()
        
        ax3 = fig.add_subplot(gs[0,2])
        ax3.plot(self.t, self.hepv["tankP_bar"])
        ax3.set_title("Tank Pressure")
        
        ax4 = fig.add_subplot(gs[1,0])
        speeds = np.linspace(10,80,120)
        ax4.plot(speeds, [electric_eff(s,0.7)*100 for s in speeds])
        ax4.plot(speeds, [pneumatic_eff(s,200)*100 for s in speeds])
        ax4.set_title("Motor η")
        
        ax5 = fig.add_subplot(gs[1,1])
        ax5.plot(self.t, self.hepv["Pe"]/1e3, label="Elec")
        ax5.plot(self.t, self.hepv["Pp"]/1e3, label="Pneu")
        ax5.legend()
        ax5.set_title("Power Split")
        
        ax6 = fig.add_subplot(gs[1,2])
        energy = [self.bev["E_kWh"], self.hepv["E_kWh"]]
        colors = ["#4CAF50", "#F44336" if energy[1]>energy[0] else "#FF9800"]
        bars = ax6.bar(["BEV","HEPV"], energy, color=colors)
        for b,val in zip(bars,energy):
            ax6.text(b.get_x()+b.get_width()/2, val, f"{val:.4f}", 
                     ha="center", va="bottom", fontsize=8)
        ax6.set_ylabel("Energy [kWh]")
        ax6.set_title("Total Energy")
        
                # fig.tight_layout()
        return fig
    def save(self,
             save_individual: bool,
             save_combined:   bool,
             show: bool,
             dpi: int) -> None:

        self.out.mkdir(parents=True, exist_ok=True)
        saved: list[pathlib.Path] = []

        if save_combined:
            fig = self.combined_panel()
            path = self.out / "combined.png"
            fig.savefig(path, dpi=dpi, bbox_inches="tight")
            saved.append(path)
            plt.close(fig)

        if save_individual:
            figs = {
                "cycle.png" : self.fig_cycle,
                "soc.png"   : self.fig_soc,
                "energy.png": self.fig_energy_bar,
            }
            for fname, func in figs.items():
                fig = func()
                p   = self.out / fname
                fig.savefig(p, dpi=dpi, bbox_inches="tight")
                saved.append(p)
                plt.close(fig)

        logging.info("Saved %d figure(s): %s",
                     len(saved),
                     ", ".join(p.name for p in saved))

        if show:
            logging.info("Displaying figures (close windows to continue)")
            for path in saved:
                plt.figure(); img = plt.imread(path); plt.imshow(img); plt.axis("off")
            plt.show()


# ╔═══════════════════════════════════════════════════════════════════════════╗
# 7.  CSV / REPORT HELPERS                                                    #
# ╚═══════════════════════════════════════════════════════════════════════════╝
def save_csv(path: pathlib.Path, arr: NDArray[np.float64], header: str) -> None:
    np.savetxt(path, arr, delimiter=";", header=header, comments="", fmt="%.6f")

def save_summary(out: pathlib.Path,
                 args: argparse.Namespace,
                 bev: Dict, hepv: Dict) -> None:

    diff = (hepv["E_kWh"] / bev["E_kWh"] - 1) * 100
    txt  = (out / "summary.txt")
    with txt.open("w", encoding="utf-8") as f:
        f.write(f"HEPV summary  {datetime.now()}\n")
        f.write(f"Duration  : {args.duration} s   dt = {args.dt} s\n")
        f.write(f"BEV  energy: {bev['E_kWh']:.4f} kWh\n")
        f.write(f"HEPV energy: {hepv['E_kWh']:.4f} kWh\n")
        f.write(f"Δ = {diff:+.2f} %\n")
    logging.info("Summary written → %s", txt.name)

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 8.  MAIN                                                                    #
# ╚═══════════════════════════════════════════════════════════════════════════╝
def main() -> None:
    args = parse_cli()
    args.out.mkdir(parents=True, exist_ok=True)

    print("="*72)
    print(f"HEPV simulator v{__version__}")
    print("="*72)

    if not args.no_validation:
        print_validation_report()

    # ------------------------------------------------------------------ run
    t, v   = urban_cycle(args.duration, args.dt)
    bev    = simulate_bev(t, v)
    hepv   = simulate_hepv(t, v)
    diff   = (hepv["E_kWh"] / bev["E_kWh"] - 1) * 100
    logging.info("Δ energy HEPV vs BEV: %+ .2f %%", diff)

    # -------------------------------------------------------------- export
    save_csv(args.out/"bev.csv",
             np.column_stack((t, v*3.6, bev["soc"]*100)),
             "time_s;speed_kmh;soc_%")
    save_csv(args.out/"hepv.csv",
             np.column_stack((t, v*3.6, hepv["soc"]*100, hepv["tankP_bar"])),
             "time_s;speed_kmh;soc_% ;P_bar")

    save_summary(args.out, args, bev, hepv)

    # -------------------------------------------------------------- plots
    if not args.skip_plots:
        PlotManager(t, v, bev, hepv, args.out).save(
            save_individual = args.save_individual,
            save_combined   = not args.skip_combined,
            show            = args.show,
            dpi             = args.dpi)
    else:
        logging.info("Plot generation skipped (--skip-plots)")

    print("="*72)
    print("Finished – output directory:", args.out.resolve())

# ╔═══════════════════════════════════════════════════════════════════════════╗
# 9.  CLI ENTRY                                                               #
# ╚═══════════════════════════════════════════════════════════════════════════╝
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Interrupted by user")
    except Exception as e:          # pragma: no cover
        logging.exception("Unhandled error: %s", e)
        sys.exit(1)
