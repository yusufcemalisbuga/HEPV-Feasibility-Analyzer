# HEPV Feasibility Analyzer

<div align="center">

### 🔋⚡ Hybrid Electric-Pneumatic Vehicle Simulator
**Rigorous thermodynamic analysis of compressed air hybridization in urban micro-mobility**

[![Conference](https://img.shields.io/badge/ECP%202025-Accepted-success?logo=academia)](https://ecp2025.sciforum.net/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-3.3.0--alpha-orange)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)
[![DOI](https://img.shields.io/badge/DOI-10.3390%2Fecp2025--XX-blue)](https://sciforum.net/paper/view/24624)

[**Quick Start**](#-quick-start) • [**Results**](#-key-findings) • [**Research Evolution**](#-research-evolution) • [**Documentation**](#-technical-documentation) • [**Citation**](#-citation)

---

<img src="https://img.shields.io/badge/Status-Under_Peer_Review-blueviolet?style=for-the-badge" alt="Status"/>

**Author:** [Yusuf Cemal ISBUGA](https://orcid.org/0009-0001-7565-9753)  
**Presented at:** 4th International Electronic Conference on Processes 2025

</div>

---

## 🎯 Research Question

> **Can pneumatic-electric hybrids compete with pure battery EVs in urban applications when modeled with physically accurate thermodynamics?**

This single-file Python simulator provides a **transparent, reproducible computational framework** to answer this question through:

- ✅ Validated against Tesla Model 3 motor data (MotorXP teardown)
- ✅ Industrial pneumatic motor efficiency curves (Atlas Copco, Parker Hannifin)
- ✅ Real-world comparison with Peugeot Hybrid Air trials (2013-2015)
- ✅ First-principles thermodynamics with heat transfer & leakage
- ✅ Complete version history showing honest research iteration

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer.git
cd HEPV-Feasibility-Analyzer

# Install dependencies (numpy + matplotlib only)
pip install -r requirements.txt

# Run default simulation (400s urban cycle, 150 bar initial)
python hepv.py
```

### Basic Usage

```bash
# Show plots interactively
python hepv.py --show

# Extended simulation with debugging
python hepv.py --duration 600 --verbose

# Export all outputs
python hepv.py --save-individual --dpi 600

# Custom output directory
python hepv.py --out ~/my_results
```

**Output:** `~/hepv_results/` contains:
- `combined.png` – 3×3 analysis dashboard
- `bev.csv`, `hepv.csv` – Time-series data
- `summary.txt` – Energy comparison report

---

## 📊 Key Findings

<div align="center">

### Energy Consumption Comparison

| Configuration | Version | Energy | vs BEV | Status |
|--------------|---------|--------|--------|--------|
| **BEV Baseline** | All | 0.XXXX kWh | — | ✅ Reference |
| **HEPV Passive** | v1.0 | +11.08% | ❌ Worse | Confirmed failure |
| **HEPV Active** | v3.0 | **−5.18%** | ⚠️ Better | **Suspicious** |
| **HEPV Corrected** | v3.3.0 | 🔬 TBD | ❓ | **Under validation** |

</div>

### ⚠️ Critical Discovery (v3.3.0)

**Thermodynamic sign error found in tank pressure calculation:**

```python
# WRONG (v1.0-3.0): Tank gained pressure during discharge
dP = -E * (n - 1.0) / V  # Violated conservation of energy

# FIXED (v3.3.0): Correct thermodynamic sign
dP = E * (n - 1.0) / V   # Pressure decreases when extracting energy
```

**Impact:** Previous v3.0 results (−5.18% improvement) now **under re-evaluation** with corrected physics.

---

## 🔬 Research Evolution

<details>
<summary><b>📅 Version History (Click to expand)</b></summary>

### v1.0 (2025-01-08) — Passive Control

```
Configuration:
├─ Tank: Started at atmospheric pressure (1 bar)
├─ Strategy: Conservative thresholds
├─ Usage: 0 pneumatic activations
└─ Result: +11.08% penalty ❌

Conclusion: Confirmed commercial failures (Peugeot, MDI AirPod)
```

### v3.0 (2025-01-19) — Active Optimization

```
Configuration:
├─ Tank: Pre-pressurized to 300 bar
├─ Strategy: Optimized triggers (v<35km/h, P>3kW, SoC>0.2)
├─ Usage: 360 activations (9% of cycle)
└─ Result: −5.18% improvement ⚠️

Red flags:
- 300 bar pre-charge energy not accounted for
- Sign error allowed impossible pressure increases
- Used compressor η (60%) instead of motor η (25-45%)
```

### v3.3.0-alpha (Current) — Thermodynamic Corrections

```
Critical fixes:
✅ Tank thermodynamics sign bug (dP = E·(n-1)/V)
✅ Real pneumatic motor η during discharge (not compressor η)
✅ Initial tank energy properly calculated from P_init
✅ Professional logging system (DEBUG/INFO/WARNING/ERROR)
✅ Realistic regen efficiency = motor_eff(speed,0.2) × η_inverter
✅ Reduced tank pressure limits (150 bar default, 250 bar regen max)

Status: Under investigation 🔬
```

</details>

### Why This Matters

This evolution demonstrates **honest scientific iteration**:
1. **v1.0:** Negative result aligned with real-world failures ✅
2. **v3.0:** Positive result too good to be true → investigation ⚠️
3. **v3.3.0:** Root cause found → fundamental physics violated 🔧

---

## 🛠️ Technical Documentation

<details>
<summary><b>⚙️ System Parameters</b></summary>

| Parameter | BEV | HEPV (v3.3.0) | Notes |
|-----------|-----|---------------|-------|
| **Vehicle Mass** | 450 kg | 500 kg | +50 kg pneumatic hardware |
| **Battery Capacity** | 5 kWh | 5 kWh | Li-ion, same for both |
| **Motor Peak Power** | 15 kW | 15 kW | Traction motor |
| **Tank Volume** | N/A | 50 L | Carbon fiber @ 700 bar rated |
| **Tank Pressure Range** | N/A | 100-300 bar | Operating window |
| **Initial Pressure** | N/A | **150 bar** | ⬇️ Reduced from 300 |
| **Compressor η** | N/A | 60% | Regen charging |
| **Pneumatic Motor η** | N/A | 25-45% | Speed/pressure dependent |
| **Leak Rate** | N/A | 2%/min | Conservative seal assumption |

</details>

<details>
<summary><b>🧮 Physics Models</b></summary>

### Electric Motor Efficiency

```python
def electric_eff(speed_kmh, load_fraction):
    """
    Validated against Tesla Model 3 teardown (MotorXP 2018)
    - Peak: 92.12% @ 4,275 RPM, 91% load
    - Partial load: 85-90%
    - Low speed: 75-80%
    """
```

### Pneumatic Motor Efficiency

```python
def pneumatic_eff(speed_kmh, pressure_bar):
    """
    Based on Atlas Copco LZB & Parker Hannifin datasheets
    - Optimal: 40% @ 100-200 bar, <40 km/h
    - Degrades: High speeds, extreme pressures
    - Range: 15-45% (realistic industrial data)
    """
```

### Polytropic Thermodynamics

```python
def tank_thermodynamics(Pa, T, Power, dt, charging, eta):
    """
    Energy balance with heat transfer:
    - Compression: n=1.30, η=60%
    - Expansion: n=1.25, η=variable
    - Newton cooling: 10% convective coefficient
    - Leakage: 2%/min pressure loss
    
    ✅ CORRECTED: dP = E·(n-1)/V (proper sign convention)
    """
```

</details>

<details>
<summary><b>🎮 Control Strategy</b></summary>

### Pneumatic Activation Logic (v3.3.0)

```python
if (speed < 35 km/h              # Low-speed torque demand
    AND pressure > 100 bar       # Sufficient stored energy
    AND power_demand > 3 kW      # High-torque event (acceleration)
    AND battery_soc > 0.2        # Avoid deep discharge
    AND tank_energy > 1 kJ):     # Minimum energy threshold
    
    P_pneumatic = 0.35 * P_total  # 35% from compressed air
    P_electric  = 0.65 * P_total  # 65% from battery
```

### Regenerative Braking Strategy

```python
if (braking 
    AND battery_soc < 0.3 
    AND tank_pressure < 250 bar):
    
    P_battery = 0.75 * P_regen    # 75% to battery
    P_tank    = 0.25 * P_regen    # 25% recharge air tank
```

**Note:** Tank pressure limit reduced from 280 bar (v3.0) to **250 bar** (v3.3.0) for realistic fast-fill limitations.

</details>

<details>
<summary><b>📈 Validation Framework</b></summary>

### Built-in Reference Database

```python
class ValidationDB:
    TESLA_M3 = {
        "source": "MotorXP Teardown Analysis (2018)",
        "peak_efficiency": 0.9212,
        "peak_rpm": 4275,
        "peak_power_kW": 192.4
    }
    
    INDUSTRIAL_PNEUMATIC = {
        "sources": ("Atlas Copco LZB", "Parker Hannifin"),
        "efficiency_range": (0.25, 0.45),
        "optimal_pressure_bar": (6, 8)  # Industrial 6-8 bar optimal
    }
    
    PEUGEOT_TRIALS = {
        "claimed_saving": 0.45,  # 45% fuel reduction claim
        "actual_saving": 0.12,   # 12% real-world result
        "outcome": "Project discontinued 2015"
    }
```

Run `python hepv.py` to see validation report on startup.

</details>

---

## 🎓 Academic Context

### Conference Publication

**Title:** *Hybrid Electric-Pneumatic Vehicles: Feasibility Analysis and Practical Limitations*  
**Venue:** 4th International Electronic Conference on Processes (ECP 2025)  
**URL** [GO](https://sciforum.net/paper/view/24624)  
**Status:** Accepted – Under peer review

### Comparison with Literature

| System | Study | Claimed | Actual | Outcome |
|--------|-------|---------|--------|---------|
| **Hybrid Air** | Peugeot (2013-15) | 45% | 12% | Discontinued |
| **AirPod** | MDI | 200 km | <80 km | Commercial failure |
| **HEPV v1.0** | This study | N/A | −11% | Aligns with failures ✅ |
| **HEPV v3.0** | This study | N/A | **−5%** | **Too optimistic** ⚠️ |
| **HEPV v3.3.0** | This study | N/A | 🔬 **TBD** | Under validation |

### Research Contributions

1. **Transparent Methodology**
   - Single-file implementation (zero hidden dependencies)
   - Complete version history with negative results
   - Open-source reproducibility

2. **Rigorous Validation**
   - Industrial motor efficiency data
   - Real-world failure case studies
   - First-principles thermodynamics

3. **Critical Self-Review**
   - Discovered and documented own errors
   - Simulation-reality gap analysis
   - Honest uncertainty quantification

---

## 📦 Advanced Usage


### Output Files

```
~/hepv_results/
├── combined.png          # 3×3 analysis dashboard
├── cycle.png             # Speed profile
├── soc.png               # Battery state-of-charge
├── energy.png            # Energy comparison bar chart
├── bev.csv               # BEV time-series (time;speed;soc)
├── hepv.csv              # HEPV time-series (time;speed;soc;pressure)
└── summary.txt           # Text report with energy delta
```

### Code Structure

```python
hepv.py (~800 lines, single file)
│
├─ 0. LOGGING & CLI           # argparse + logging setup
├─ 1. VALIDATION DATABASE     # Tesla M3, industrial references
├─ 2. PARAMETERS              # Frozen dataclass (immutable)
├─ 3. PHYSICS MODELS          # Efficiency maps + thermodynamics
├─ 4. DRIVING CYCLE           # WLTP-inspired urban pattern
├─ 5. SIMULATORS              # BEV & HEPV forward integration
├─ 6. PLOT MANAGER            # Matplotlib visualizations
├─ 7. CSV/REPORT HELPERS      # Data export utilities
├─ 8. MAIN                    # Orchestration logic
└─ 9. CLI ENTRY               # if __name__ == "__main__"
```

---

## 🔮 Roadmap

### ✅ Completed (v3.3.0)

- [x] Fix thermodynamic sign error
- [x] Implement proper initial energy calculation
- [x] Add comprehensive logging system
- [x] Validate against industrial data
- [x] Document research evolution

### 🎯 Immediate (Pre-Conference)

- [ ] Complete sensitivity analysis (tank size, pressure, thresholds)
- [ ] Validate against Peugeot field trial data
- [ ] Monte Carlo uncertainty quantification
- [ ] Document all assumptions and limitations

### 🚀 Short-Term (Post-Conference)

- [ ] Multi-cycle comparison (highway, mixed urban/highway)
- [ ] Economic analysis (system cost vs. energy savings)
- [ ] Machine learning-based control optimization
- [ ] Experimental validation roadmap

### 🌟 Long-Term Vision

- [ ] Lab test rig validation
- [ ] Industry collaboration (pneumatic hardware suppliers)
- [ ] Peer-reviewed journal publication
- [ ] GUI for non-technical users

---

## 📚 Citation

### BibTeX (Software)

```bibtex
@software{isbuga2025hepv,
  title   = {HEPV Feasibility Analyzer: Thermodynamic Simulation of 
             Hybrid Electric-Pneumatic Vehicles},
  author  = {ISBUGA, Yusuf Cemal},
  year    = {2025},
  version = {3.3.0-alpha},
  url     = {https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer},
  note    = {Presented at 4th International Electronic Conference on 
             Processes (ECP 2025)}
}
```

### BibTeX (Conference Paper)

```bibtex
@inproceedings{isbuga2025hepv_paper,
  title     = {Hybrid Electric-Pneumatic Vehicles: Feasibility Analysis 
               and Practical Limitations},
  author    = {ISBUGA, Yusuf Cemal},
  booktitle = {Proceedings of the 4th International Electronic 
               Conference on Processes},
  year      = {2025},
  publisher = {MDPI},
  doi       = {N/A},
  url       = {https://sciforum.net/paper/view/24624}
}
```

---

## 🤝 Contributing

### We Welcome

- 🐛 **Bug reports** – Thermodynamic inconsistencies, numerical errors
- 💡 **Feature requests** – Alternative control strategies, driving cycles
- 🔬 **Validation data** – Experimental results, industrial case studies
- 📖 **Documentation improvements** – Clarifications, translations
- 🧪 **Code contributions** – Optimization, new physics models

### Seeking Collaboration

- **Experimental validation:** Test rig design, lab partnerships
- **Control theory:** Model Predictive Control, reinforcement learning
- **CFD validation:** Thermodynamic model refinement
- **Peer review:** Methodology critique, sensitivity analysis
- **Industry:** Pneumatic hardware suppliers, automotive research labs

### Contact

**Yusuf Cemal ISBUGA**  
📧 yisbuga37@gmail.com  
🔗 [GitHub](https://github.com/yusufcemalisbuga)  
🌐 [ORCID](https://orcid.org/0009-0001-7565-9753)

---

## ⚠️ Disclaimer

### Current Status: THERMODYNAMIC CORRECTIONS UNDER VALIDATION

**v3.3.0-alpha represents fundamental physics corrections:**

✅ **Fixed:** Sign error in pressure calculation  
✅ **Fixed:** Efficiency application (motor vs. compressor)  
✅ **Fixed:** Initial energy state consistency  
🔬 **Pending:** Results validation with corrected thermodynamics

### Known Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| **Energy accounting** | Compression energy to 150 bar not in comparison | Document initial state assumptions |
| **Mechanical losses** | Valve dynamics, pneumatic friction simplified | Conservative efficiency estimates |
| **Thermal effects** | Heat exchanger idealized (10% coefficient) | Sensitivity analysis planned |
| **Cycling degradation** | Frequent charge/discharge losses not modeled | Include in future versions |
| **Environmental factors** | Temperature, traffic, driver variability excluded | Statistical analysis needed |

### Recommendation

**Treat all results as UPPER BOUND until experimental validation.**

The dramatic evolution from:
- v1.0: **+11% penalty** → Confirmed failure ✅
- v3.0: **−5% improvement** → Suspicious ⚠️
- v3.3.0: **TBD** → Under honest reassessment 🔬

demonstrates **extreme sensitivity** to:
- Control strategy assumptions
- Thermodynamic model accuracy
- Initial condition choices

---

## 📜 License

MIT License – Free for academic and commercial use with attribution.

```
Copyright (c) 2025 Yusuf Cemal ISBUGA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Full text: [LICENSE](LICENSE)

---

<div align="center">

## 🟡 Project Status

**v1.0:** Passive control → Simulated commercial failure  
**v3.0:** Active control → Unexpectedly positive (red flag detected)  
**v3.3.0:** Corrected physics → **Honest reassessment in progress**

---

### *"In science, there is no shame in finding your code was wrong.*  
### *The shame is in not fixing it when you do."*

---

⭐ **Star this repository to follow the validation journey!**

[![GitHub stars](https://img.shields.io/github/stars/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=social)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)
[![GitHub forks](https://img.shields.io/github/forks/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=social)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer/fork)
[![GitHub watchers](https://img.shields.io/github/watchers/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=social)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)

**Made with ❤️ for open science • Last updated: January 2025**

</div>
