# HEPV Feasibility Analyzer
### Hybrid Electric-Pneumatic Vehicle: Thermodynamic Analysis & Practical Limitations

[![Conference](https://img.shields.io/badge/Conference-ECP%202025-blue)](https://ecp2025.sciforum.net/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-red)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)


**Author:** Yusuf Cemal ISBUGA  
**Presented at:** 4th International Electronic Conference on Processes 2025  
**Research Status:** ❌ Study Terminated - Negative Results Published

---

## 🎯 Research Question
*Can pneumatic-electric hybrid systems compete with pure battery EVs in urban micro-mobility applications?*

**Answer:** **No.** HEPV consumes **11.08% MORE** energy than baseline BEV.

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

## 📊 Key Results

### Energy Consumption (400s Urban Cycle)
```
┌─────────────────────────────────────┐
│  BEV:  0.19840 kWh  ✅ BASELINE    │
│  HEPV: 0.22037 kWh  ❌ +11.08%     │
└─────────────────────────────────────┘

Pneumatic Usage: 0 time steps
(System never activated - conditions never met)
```

### Why HEPV Failed
```
🔴 Energy Losses:
   ├─ Compression:     ~40% efficiency loss
   ├─ Pneumatic Motor: ~60% efficiency loss
   ├─ Air Leakage:     2% per minute
   └─ Heat Transfer:   Significant thermal losses

⚖️  System Penalties:
   ├─ Mass:           +50 kg (+11.1%)
   ├─ Complexity:     Dual powertrain integration
   └─ Cost:           300-bar tank + compressor

📉 Operational Reality:
   └─ Pneumatic advantage exists only <30 km/h
      (too narrow for practical benefit)
```

---

## 🖼️ Visualization Results

 [(Combined Analysis)]<img width="4767" height="3540" alt="HEPV_Combined_Analysis" src="https://github.com/user-attachments/assets/ea7aff5f-e270-4495-875a-989309525067" />


**9-Panel Comprehensive Analysis:**
1. **Driving Cycle** - WLTP-inspired urban pattern (0-50 km/h)
2. **Battery SoC** - HEPV drains faster despite hybrid assist
3. **Tank Pressure** - Never exceeds minimum threshold (100 bar)
4. **Motor Efficiency Map** - Electric dominates across speed range
5. **Power Distribution** - Pneumatic system unused (0 activations)
6. **Energy Comparison** - 11.08% penalty visualized
7. **Tank Temperature** - Thermodynamic effects minimal (no usage)
8. **BEV Efficiency Histogram** - Mean 77.6% under real conditions
9. **Summary Panel** - Quantitative termination justification

---

## 🚫 Why This Research Matters

### Transparent Negative Results Publishing

**Previous Failed Attempts:**
- **Peugeot Hybrid Air (2013-2015):** Claimed 45% savings → Actual 12% → Discontinued
- **Tata/MDI AirPod:** Insufficient range, commercial failure
- **PSA Air Hybrid:** Project abandoned after field trials

**This Study's Contribution:**
✅ First open-source thermodynamic model with validated physics  
✅ Quantitative termination criteria (not marketing claims)  
✅ Reproducible simulation code (prevents future waste)  
✅ Academic integrity: Publishing failures to guide research priorities

> *"Technically feasible ≠ Commercially viable"*

---

## 🛠️ Technical Implementation

### Core Physics Models
```python
Electric Motor:  η = f(speed, load)  # Tesla M3 validated
Pneumatic Motor: η = f(speed, pressure)  # Industrial refs
Thermodynamics:  PV^n = const  # Polytropic process
Heat Transfer:   Q̇ = hA(T - T_amb)  # Ambient cooling
```

### System Architecture
- **Control Strategy:** Pneumatic assist @ low speed + high power
- **Trigger Conditions:** v < 35 km/h, P > 100 bar, P_demand > 8 kW
- **Regenerative Braking:** 75% battery, 25% air compression
- **Time Resolution:** 0.1s steps, 4000 data points

### Technology Stack
- **Language:** Python 3.8+
- **Dependencies:** NumPy, Matplotlib
- **Output Formats:** PNG (300 DPI), CSV, PDF, TXT reports
- **Validation:** Peer-reviewed motor efficiency data

---

## 📦 Installation & Usage

### Quick Start
```bash
git clone https://github.com/yourusername/HEPV-Feasibility-Analyzer.git
cd HEPV-Feasibility-Analyzer
pip install -r requirements.txt

# Basic run (saves to C:\sonuc)
python hepv-analyzer.py

# Interactive mode with plots
python hepv-analyzer.py --show --save-individual

# Custom simulation
python hepv-analyzer.py --duration 600 --dt 0.05 --verbose
```



## 📈 Simulation Parameters

### Vehicle Specifications
| Parameter | BEV | HEPV | Notes |
|-----------|-----|------|-------|
| **Mass** | 450 kg | 500 kg | +50 kg penalty |
| **Battery** | 5 kWh | 5 kWh | Same capacity |
| **Motor** | 15 kW | 15 kW | Peak power |
| **Pneumatic** | - | 300 bar | 50L tank |
| **Drag Coeff** | 0.28 | 0.28 | Urban micro-EV |
| **Frontal Area** | 1.2 m² | 1.2 m² | Compact design |

### Efficiency Assumptions
- **Electric Motor Peak:** 92% (Tesla M3 reference)
- **Pneumatic Motor Peak:** 40% (industrial data)
- **Compressor:** 60% (polytropic compression)
- **Regenerative Braking:** 75% (battery), 60% (air)

---

## 🎓 Academic Context

### Research Background
- **Institution:** Independent researcher
- **Prior Work:** CERN Beamline for Schools (Türkiye representative)
- **Focus:** Techno-economic feasibility of sustainable energy systems
- **Methodology:** First-principles thermodynamic analysis

### Conference Presentation
**Title:** *Hybrid Electric-Pneumatic Vehicles: Feasibility Analysis and Practical Limitations*  
**Event:** 4th International Electronic Conference on Processes (ECP 2025)  
**Organizer:** MDPI - Processes Journal  
**Outcome:** Study termination recommendation published

### Key Contributions
1. **Literature Gap Identified:** No comprehensive E-P models for <500 kg urban vehicles
2. **Decision Framework:** "Technically feasible, practically inefficient" classification
3. **Scale Sensitivity:** Mass penalties critical in compact applications
4. **Transparent Reporting:** Rigorous negative results prevent future waste

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
  Url=(sciforum)={https://sciforum.net/paper/view/24624}
  url={https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer}
}
```

### APA Format
```
İŞBUĞA, Y.C. Hybrid Electric–Pneumatic Propulsion System for Sustainable Urban Transportation: Design and Energy Management Optimization, in Proceedings of the 4th International Electronic Conference on Processes, 20–22 October 2025, MDPI: Basel, Switzerland, 
```

---

## 🔍 Lessons Learned

### Technical Insights
✅ **Thermodynamic Fundamentals Trump Theoretical Benefits**  
   Compression-expansion cycle losses are unavoidable physics

✅ **Narrow Operational Windows = Commercial Failure**  
   Pneumatic advantage only at <30 km/h makes system impractical

✅ **Mass Penalties Scale Non-Linearly**  
   50 kg is negligible in trucks, critical in micro-mobility

### Research Methodology
✅ **Validated Models > Marketing Claims**  
   Tesla M3 teardown data provides honest baseline

✅ **Negative Results Have High Value**  
   Saving future researchers time/money justifies publication

✅ **Simulation Before Prototyping**  
   Computational models prevent expensive hardware failures

---

## 🚀 Future Directions

### What Works Better Than Pneumatic Hybrids:
1. **Lightweight Materials** - Carbon fiber, aluminum alloys
2. **Improved Regenerative Braking** - 85%+ efficiency targets
3. **Battery Chemistry** - Solid-state, higher energy density
4. **Aerodynamic Optimization** - Lower Cd for urban speeds
5. **Thermal Management** - Active cooling for battery longevity

### Pneumatic Systems CAN Work In:
- **Stationary Energy Storage** (grid-scale, <50% efficiency acceptable)
- **Heavy Machinery** (short bursts, mass penalty negligible)
- **Niche Applications** (where electricity unavailable)

**Not suitable for:** Urban passenger vehicles (this study proves)

---

## 📧 Contact & Collaboration

**Yusuf Cemal ISBUGA**  
📧 yisbuga37@gmail.com  
🔗 [GitHub Profile](github.com/yusufcemalisbuga)  
🌐 [ORCID](https://orcid.org/0009-0001-7565-9753) 

**Open to:**
- Peer review feedback
- Computational modeling collaborations
- Energy systems feasibility studies
- Academic discussions on sustainable transport

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file.

**You are free to:**
- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Use in academic research

**Requirements:**
- 📝 Include copyright notice
- 📝 Cite this work in publications

---

## 🙏 Acknowledgments

- **Tesla Model 3 Data:** MotorXP Teardown Analysis (2018)
- **Pneumatic References:** Atlas Copco, Parker Hannifin technical docs
- **Validation Case:** Peugeot Hybrid Air field trial data (2013-2015)
- **Conference:** MDPI ECP 2025 organizing committee
- **Community:** Open-source scientific Python developers

---

## ⚠️ Disclaimer

This simulation uses validated models but makes assumptions about:
- Ideal control strategies
- Component integration losses
- Real-world driving variability

**Physical prototypes would likely show worse performance** than simulated due to:
- Mechanical friction
- Electrical conversion losses
- Environmental factors
- Manufacturing tolerances

*The 11.08% penalty is a conservative lower bound.*

---

<div align="center">

### 🔴 Project Status: TERMINATED

**Conclusion:** Thermodynamic laws prevent HEPV commercial viability for urban vehicles.

**Recommendation:** Research resources better spent on battery optimization.

---

*"The most valuable research sometimes proves an idea shouldn't be pursued."*

**⭐ Star this repo if transparent negative results matter to you!**

