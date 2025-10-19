

# HEPV Feasibility Analyzer
### Hybrid Electric-Pneumatic Vehicle: Thermodynamic Analysis & Control Optimization

[![Conference](https://img.shields.io/badge/Conference-ECP%202025-blue)](https://ecp2025.sciforum.net/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Under_Review-orange)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)

**Author:** Yusuf Cemal ISBUGA  
**Presented at:** 4th International Electronic Conference on Processes 2025  
**Research Status:** 🟡 Under Investigation - Control Strategy Sensitivity Analysis

---

## 🎯 Research Question
*Can pneumatic-electric hybrid systems compete with pure battery EVs in urban micro-mobility with optimized control strategies?*

**Latest Finding:** 5.18% efficiency **improvement** with active power management (360 pneumatic activations)

---

## 🔄 Research Evolution

### Version History
```
v1.0 (2025-01-08): Passive Control Strategy
├─ Tank Initial State: Atmospheric pressure (1 bar)
├─ Trigger Conditions: Conservative thresholds
├─ Pneumatic Usage: 0 activations
└─ Result: +11.08% penalty ❌

v3.0 (2025-01-19): Active Control Optimization
├─ Tank Initial State: Pre-pressurized (300 bar)
├─ Trigger Conditions: Optimized (v<35km/h, P>3kW, SoC>0.2)
├─ Pneumatic Usage: 360 activations (9% of cycle)
└─ Result: -5.18% improvement ⚠️
```

**Critical Observation:** 16.26% swing demonstrates **control strategy dominates hardware**.

---

## 🔬 What This Project Does

Rigorous computational simulation comparing:
- **BEV** (Pure Battery Electric Vehicle) - 450 kg baseline
- **HEPV** (Hybrid Electric-Pneumatic) - 500 kg with 300-bar air tank

**Validated Physics Models:**
- ✅ Tesla Model 3 electric motor (92.12% peak efficiency @ 4275 RPM)
- ✅ Industrial pneumatic motors (Atlas Copco/Parker Hannifin: 25-45% range)
- ✅ Polytropic compression/expansion with heat transfer
- ✅ WLTP-inspired urban driving cycle (400s simulation)

---

## 📊 Latest Results (v3.0)

### Energy Consumption (400s Urban Cycle)
```
┌─────────────────────────────────────┐
│  BEV:  0.19840 kWh  ✅ BASELINE    │
│  HEPV: 0.18812 kWh  ✅ -5.18%      │
└─────────────────────────────────────┘

Pneumatic Usage: 360 time steps (9% of driving cycle)
Tank Pressure: 300 bar → 200 bar (active discharge)
```

### Why Results Changed
```
🟢 Control Improvements:
   ├─ Pre-pressurized tank (300 bar initial vs 1 bar)
   ├─ Lower power threshold (3 kW vs 8 kW)
   ├─ Active pneumatic assist at urban speeds (<35 km/h)
   └─ 360 activations distributed across acceleration phases

⚠️  Critical Questions:
   ├─ Is 300 bar pre-charge realistic? (energy cost not included)
   ├─ Tank cycling losses (frequent charge/discharge)
   ├─ Real-world friction vs simulation assumptions
   └─ Peugeot Hybrid Air achieved only 12% savings (claimed 45%)
```

---

## 🖼️ Visualization Results
<img width="4766" height="3540" alt="HEPV_Combined_Analysis" src="https://github.com/user-attachments/assets/33ecdcd8-bcd1-4cdc-b95c-a7761a0500f8" />


**9-Panel Analysis (v3.0):**
1. **Driving Cycle** - WLTP-inspired urban pattern (0-50 km/h)
2. **Battery SoC** - HEPV shows slower discharge
3. **Tank Pressure** - 300→~200 bar gradual depletion
4. **Motor Efficiency Map** - Electric still dominates at high speeds
5. **Power Distribution** - Red spikes show 360 pneumatic activations
6. **Energy Comparison** - Orange bar (HEPV) now lower
7. **Tank Temperature** - 20.2°C thermal cycling visible
8. **BEV Efficiency Histogram** - Mean 77.6% unchanged
9. **Summary Panel** - "MORE EFFICIENT" (unexpected) flagged

---

## 🔍 Critical Analysis

### ⚠️ Result Validation Required

**Positive Indicators:**
- ✅ Pneumatic motor used 360 times (9% of cycle) - **system is working**
- ✅ Tank pressure drops from 300→200 bar - **energy is extracted**
- ✅ Control triggers at optimal conditions (low speed, high power demand)
- ✅ Temperature cycling minimal (20.2°C max) - **realistic thermodynamics**

**Red Flags:**
- ⚠️ 300 bar pre-charge energy cost **not included** in comparison
- ⚠️ Peugeot Hybrid Air real-world: 12% savings (simulation claimed 45%)
- ⚠️ 5.18% improvement **contradicts v1.0** penalty (+11.08%)
- ⚠️ Frequent cycling (360 times) may introduce losses not modeled

### 🎯 Next Steps Before Conference
1. **Sensitivity Analysis:**
   - Tank initial pressure: 1 bar vs 100 bar vs 300 bar
   - Power threshold: 3 kW vs 5 kW vs 8 kW
   - Speed threshold: 25 km/h vs 35 km/h vs 45 km/h

2. **Energy Accounting:**
   - Include compression energy to reach 300 bar initial state
   - Model tank cycling degradation (pressure loss per cycle)
   - Add mechanical friction (valves, pneumatic motor wear)

3. **Literature Comparison:**
   - Validate against Peugeot Hybrid Air field data
   - Compare with MDI AirPod efficiency claims
   - Cross-reference industrial pneumatic motor datasheets

---

## 🛠️ Technical Implementation

### Core Physics Models
```python
Electric Motor:  η = f(speed, load)  # Tesla M3 validated
Pneumatic Motor: η = f(speed, pressure)  # Industrial refs (25-45%)
Thermodynamics:  PV^n = const  # Polytropic n=1.25 (expansion)
Heat Transfer:   Q̇ = hA(T - T_amb)  # 10% coefficient
```

### Control Strategy (v3.0)
```python
# Pneumatic activation conditions
use_pneumatic = (
    speed < 35 km/h AND           # Urban acceleration
    tank_pressure > 100 bar AND   # Sufficient energy stored
    power_demand > 3 kW AND       # High torque event
    battery_soc > 0.2             # Avoid deep discharge
)

# Power split when active
P_pneumatic = 0.35 * P_total      # 35% from air
P_electric = 0.65 * P_total       # 65% from battery
```

### Key Parameters
| Parameter | BEV | HEPV (v3.0) | Notes |
|-----------|-----|-------------|-------|
| **Mass** | 450 kg | 500 kg | +50 kg penalty |
| **Battery** | 5 kWh | 5 kWh | Same capacity |
| **Tank Initial** | N/A | **300 bar** | **Critical assumption** |
| **Activations** | 0 | **360** | 9% of cycle |
| **Pneumatic Efficiency** | N/A | ~32% avg | Speed-dependent |

---

## 📦 Installation & Usage

### Quick Start
```bash
git clone https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer.git
cd HEPV-Feasibility-Analyzer
pip install -r requirements.txt

# Run v3.0 with optimized control
python hepv-analyzer.py

# Save all individual plots
python hepv-analyzer.py --save-individual --dpi 300

# Custom output location
python hepv-analyzer.py --out /path/to/output
```


---

## 🎓 Academic Context

### Conference Presentation
**Title:** *Hybrid Electric-Pneumatic Vehicles: Feasibility Analysis and Practical Limitations*  
**Event:** 4th International Electronic Conference on Processes (ECP 2025)  
**URL** (https://sciforum.net/paper/view/24624)  
**Status:** Accepted - Under peer review

### Research Contributions
1. **Control Strategy Impact:** First study quantifying power management influence (16.26% swing)
2. **Transparent Iteration:** Publishing both negative (v1.0) and positive (v3.0) results
3. **Critical Self-Review:** Identifying assumptions requiring experimental validation
4. **Open-Source Model:** Reproducible code for community validation

### Comparison with Literature
| Study | System | Claimed | Actual | Outcome |
|-------|--------|---------|--------|---------|
| **Peugeot Hybrid Air** | 2.0L engine + air | 45% savings | 12% | Discontinued 2015 |
| **MDI AirPod** | Pure pneumatic | 200 km range | <80 km | Commercial failure |
| **This study (v1.0)** | EV + air (passive) | Feasible? | -11% penalty | Negative result |
| **This study (v3.0)** | EV + air (active) | Feasible? | +5% improvement | **Requires validation** |

---

## 📚 Citation

### BibTeX
```bibtex
@inproceedings{isbuga2025hepv,
  title={Hybrid Electric-Pneumatic Vehicles: Feasibility Analysis and Practical Limitations},
  author={ISBUGA, Yusuf Cemal},
  booktitle={Proceedings of the 4th International Electronic Conference on Processes},
  year={2025},
  organization={MDPI},
  note={Under peer review},
  url={https://sciforum.net/event/ECP2025}
}
```

---

## 🚀 Future Work

### Before Final Conclusions:
1. ✅ **Sensitivity Analysis** - Test all control parameters
2. ✅ **Energy Accounting** - Include compression costs
3. ✅ **Experimental Validation** - Build test rig or collaborate with lab
4. ✅ **Peer Review** - Submit findings to energy systems journal

### If Results Hold:
- Control algorithms matter **more than hardware** in hybrid systems
- Pre-charged pneumatic assist viable for **urban micro-mobility**
- Further optimization potential (ML-based power management)

### If Results Fail Validation:
- Document reasons for simulation-reality gap
- Identify missing physics (friction, cycling losses, valve dynamics)
- Publish negative results to guide future research

---

## 📧 Contact & Collaboration

**Yusuf Cemal ISBUGA**  
📧 yisbuga37@gmail.com  
🔗 [GitHub](https://github.com/yusufcemalisbuga)  
🌐 [ORCID](https://orcid.org/0009-0001-7565-9753)

**Open to:**
- Experimental validation partnerships
- Control theory optimization discussions
- Peer review feedback on methodology
- Collaboration on energy systems modeling

---

## 📜 License

MIT License - Free for academic and commercial use with attribution.

---

## ⚠️ Disclaimer

**Current Status:** Results are **simulation-based** and require experimental validation.

**Known Limitations:**
- 300 bar pre-charge energy cost not accounted for
- Valve dynamics and mechanical friction simplified
- Cycling degradation not modeled
- Real-world driving variability not captured

**Recommendation:** Treat v3.0 results as **upper bound** pending validation. The dramatic shift from v1.0 (-11%) to v3.0 (+5%) highlights sensitivity to control assumptions.

---

<div align="center">

### 🟡 Project Status: UNDER INVESTIGATION

**v1.0 Conclusion:** Passive system commercially unviable (-11% penalty)  
**v3.0 Conclusion:** Active control shows promise (+5% improvement)  
**Reality:** Likely somewhere between - **experimental validation required**

---

*"Control strategy can transform hardware from failure to success - but simulation must be validated against reality."*

**⭐ Star this repo to follow the validation process!**

[![Profile Views](https://komarev.com/ghpvc/?username=yusufcemalisbuga&color=orange&style=flat-square&label=Project+Followers)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)

</div>
```




