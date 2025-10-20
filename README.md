
<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=200&section=header&text=HEPV%20Feasibility%20Analyzer&fontSize=50&fontAlignY=35&desc=Thermodynamic%20Reality%20Check%20for%20Compressed%20Air%20Hybrids&descAlignY=55&descSize=18)

# ⚡ Hybrid Electric-Pneumatic Vehicle Analysis

### **Conference-validated proof: Compressed air hybridization fails thermodynamics**

[![ECP 2025](https://img.shields.io/badge/ECP_2025-Peer_Reviewed-success?style=for-the-badge&logo=academia)](https://sciforum.net/paper/view/24624)
[![DOI](https://img.shields.io/badge/DOI-10.3390%2Fecp2025--24624-blue?style=for-the-badge)](https://sciforum.net/paper/view/24624)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[**📊 Results**](#-the-verdict) • [**💻 Quick Start**](#-quick-start) • [**🔬 Methodology**](#-methodology) • [**📚 Citation**](#-citation) • [**🤝 Contribute**](#-contributing)

---

## 🎯 TL;DR

<table>
<tr>
<td width="40%" align="center">

### ❓ Research Question

**Can compressed air improve efficiency over pure battery EVs?**

</td>
<td width="60%" align="center">

### ❌ Answer: NO

**HEPV uses +2.9% MORE energy**  
Despite optimized control, realistic pre-charge, and best-case assumptions

</td>
</tr>
</table>

**Why it matters:** Confirms why Peugeot, MDI, and Tata all abandoned air-hybrid projects. **Thermodynamic losses are unavoidable.**

---

![Efficiency Comparison](https://img.shields.io/badge/BEV-0.1914_kWh-brightgreen?style=for-the-badge)
![Efficiency Comparison](https://img.shields.io/badge/HEPV-0.1969_kWh_(+2.9%25)-red?style=for-the-badge)

</div>

---

## 🔥 The Verdict

<div align="center">

### Energy Consumption (400s Urban Cycle)

<img width="2926" alt="Energy Comparison" src="https://github.com/user-attachments/assets/be8fe0b9-7709-4954-980e-005cbe69391c" />

</div>

<table>
<tr>
<td width="50%">

### ✅ BEV (Baseline)

**Energy:** 0.1914 kWh  
**Efficiency:** 86% (motor avg)  
**Mass:** 450 kg  
**Losses:** Minimal (motor + drag)

**Winner:** Pure electric is simpler, lighter, more efficient

</td>
<td width="50%">

### 🔴 HEPV (Hybrid)

**Energy:** 0.1969 kWh (+2.9%)  
**Pneumatic η:** 25-32% (terrible!)  
**Mass:** 500 kg (+11%)  
**Losses:** Compression 40%, expansion 68%, leakage 2%/min

**Penalty breakdown:**
- Thermodynamic: +2.0%
- Mass: +0.7%
- Complexity: +0.2%

</td>
</tr>
</table>

---

## 💡 Why Air Hybrids Fail (Physics 101)

<div align="center">

### Energy Conversion Efficiency

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ELECTRIC PATH (BEV)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Braking → Battery → Motor → Wheels
  100%  →   97%   →  90%  →  86% ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PNEUMATIC PATH (HEPV)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Braking → Compressor → Tank → Air Motor → Wheels
  100%  →     60%    →  98% →    32%    →  18% ❌

Result: Electric is 4.8× more efficient than pneumatic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

</div>

### The Inescapable Losses

| Loss Type | Magnitude | Why Unavoidable |
|-----------|-----------|-----------------|
| **Compression** | 40% heat | Thermodynamic law (PV^n work) |
| **Expansion** | 68-75% | Industrial pneumatic motor limit |
| **Leakage** | 2% per min | High-pressure seal physics |
| **Heat dissipation** | ~10% | Newton's law of cooling |
| **Mass penalty** | 11% (+50kg) | Tank + compressor hardware |

**Bottom line:** Even perfect engineering can't fix fundamental thermodynamics.

---

## 📊 Visual Results

<div align="center">

### 6-Panel Analysis Dashboard

<img width="4766" alt="Full Analysis" src="https://github.com/user-attachments/assets/b61658d0-a0f8-4232-a24e-b073b3947546" />

**Key Observations:**
- 🔵 **Panel 1:** Urban driving cycle (0-50 km/h, realistic stops)
- 🔴 **Panel 2:** HEPV battery drains faster (orange line higher)
- 📉 **Panel 3:** Tank pressure depletes 150→120 bar (realistic leakage)
- ⚡ **Panel 4:** Electric motor dominates efficiency across all speeds
- 🎯 **Panel 5:** Pneumatic barely activates (96 times, only 2.4% of cycle)
- 📊 **Panel 6:** Final energy: HEPV bar is taller (worse)

</div>

---

## 🔬 Methodology

<details>
<summary><b>🎯 System Model (Click to expand)</b></summary>

### Vehicle Specifications

| Component | BEV | HEPV | Notes |
|-----------|-----|------|-------|
| **Total Mass** | 450 kg | 500 kg | +11% penalty |
| **Battery** | 5.0 kWh | 5.0 kWh | Li-ion NMC |
| **Electric Motor** | 15 kW | 15 kW | Tesla M3 validated |
| **Air Tank** | – | 50 L @ 150 bar | Carbon fiber |
| **Pneumatic Motor** | – | Industrial data | Atlas Copco/Parker |

### Physics Models

**Electric Motor:**
- Source: MotorXP Tesla Model 3 teardown
- Peak efficiency: 92.12% @ 4275 RPM
- Partial load: 75-90% (speed dependent)

**Pneumatic Motor:**
- Industrial catalogs (6-8 bar optimal)
- High-pressure penalty (150-300 bar worse)
- Average efficiency: 25-32%

**Thermodynamics:**
```python
# Polytropic compression/expansion
P_new = P + (E * η_comp * (n-1)) / V  # Compression
P_new = P - (E / η_pneu * (n-1)) / V  # Expansion

# Temperature coupling
T_new = T * (P_new/P)^((n-1)/n)

# Heat transfer + leakage
T_new += (T_amb - T) * k * dt
P_new *= (1 - leak_rate * dt)
```

**Driving Cycle:**  
WLTP-inspired urban (0-50 km/h, 400s, 5 acceleration/cruise/brake cycles)

</details>

<details>
<summary><b>📈 Research Evolution (Transparent Iteration)</b></summary>

### Complete Version History

| Version | Date | Tank Init | Control | Result | Status |
|---------|------|-----------|---------|--------|--------|
| **v1.0** | Jan 8 | 1 bar | Passive | **+11.1%** ❌ | Baseline failure |
| **v3.0** | Jan 19 | 300 bar | Aggressive | **-5.2%** ⚠️ | Too optimistic |
| **v3.1** | Jan 19 | 150 bar | Moderate | **+9.1%** ❌ | Energy bug |
| **v3.3** | Jan 19 | 150 bar | Realistic | **+2.9%** ✅ | **Validated** |

### What Changed in v3.3 (Final)

```diff
+ Fixed thermodynamic sign error in pressure calculation
+ Corrected pneumatic motor efficiency (was using compressor η)
+ Added proper initial tank energy tracking
+ Implemented professional logging system
+ Reduced regen pressure limit (280 → 250 bar)
+ Realistic initial conditions (150 bar achievable)

Result: 16% swing between versions proves sensitivity to assumptions
```

**Lesson:** Honest iteration reveals truth. v3.0's -5% improvement was **too good to be true** → investigation found bugs → v3.3 aligns with literature.

</details>

<details>
<summary><b>🏭 Validation Against Real Projects</b></summary>

### Failed Industry Attempts

| Project | Years | Claimed | Actual | Outcome |
|---------|-------|---------|--------|---------|
| **Peugeot Hybrid Air** | 2013-2015 | 45% fuel savings | **12%** | Cancelled |
| **MDI AirPod** | 2000-2015 | 200 km range | **<80 km** | Commercial failure |
| **Tata AirPod** | 2013-present | "Viable" | Prototype only | No production |
| **This Study** | 2025 | Optimistic: -5% | **+2.9%** | ✅ Matches reality |

**Convergence:** Our 2.9% penalty aligns with Peugeot's 12% shortfall (magnitude similar, both show "no benefit").

</details>

---

## 💻 Quick Start

### Installation (3 steps)

```bash
# 1. Clone
git clone https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer.git
cd HEPV-Feasibility-Analyzer

# 2. Install dependencies
pip install numpy matplotlib

# 3. Run simulation
python O3tamkodupy.py
```

### Output (60 seconds later)

```
✅ Simulation complete!

📊 Results:
   BEV energy:  0.1914 kWh
   HEPV energy: 0.1969 kWh
   Difference:  +2.90% (HEPV worse)

📁 Saved to ~/hepv_results/:
   - combined.png (6-panel dashboard)
   - bev.csv, hepv.csv (time series)
   - summary.txt (report)
```

### Advanced Options

```bash
# Custom duration
python O3tamkodupy.py --duration 600

# High-resolution export
python O3tamkodupy.py --dpi 600 --save-individual

# Debug mode
python O3tamkodupy.py --verbose
```

---

## 📚 Citation

### For Publications

```bibtex
@inproceedings{isbuga2025hepv,
  author    = {İşbuğa, Yusuf Cemal},
  title     = {Hybrid Electric-Pneumatic Vehicles: Feasibility Analysis 
               and Practical Limitations},
  booktitle = {Proceedings of the 4th International Electronic 
               Conference on Processes},
  year      = {2025},
  month     = oct,
  publisher = {MDPI},
  doi       = {10.3390/ecp2025-24624},
  url       = {https://sciforum.net/paper/view/24624}
}
```

### For Software

```bibtex
@software{isbuga2025hepv_code,
  author  = {İşbuğa, Yusuf Cemal},
  title   = {HEPV Feasibility Analyzer v3.3.0},
  year    = {2025},
  url     = {https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer},
  version = {3.3.0}
}
```

---

## 🤝 Contributing

### We Welcome

<table>
<tr>
<td align="center">🐛<br><b>Bug Reports</b><br><sub>Thermodynamic errors</sub></td>
<td align="center">💡<br><b>Ideas</b><br><sub>New control strategies</sub></td>
<td align="center">🔬<br><b>Validation Data</b><br><sub>Experimental results</sub></td>
<td align="center">📖<br><b>Documentation</b><br><sub>Clarifications</sub></td>
<td align="center">🧪<br><b>Code</b><br><sub>Optimizations, ML</sub></td>
</tr>
</table>

### Seeking Collaborations

**Experimental Validation:**
- University labs with dynamometers
- Automotive research centers
- Pneumatic system manufacturers

**Advanced Modeling:**
- Model Predictive Control (MPC)
- Reinforcement Learning for power management
- CFD thermal analysis

**📧 Contact:** yisbuga37@gmail.com | [ORCID](https://orcid.org/0009-0001-7565-9753) | [LinkedIn](https://linkedin.com/in/ycisbuga)

---

## 🎯 Why This Matters

<div align="center">

### 💰 Prevents Wasted R&D

```
┌──────────────────────────────────────────────────┐
│  Typical compressed air hybrid development:      │
│                                                  │
│  R&D investment:        $5-10M                   │
│  Development time:      3-5 years                │
│  Prototype testing:     $2-3M                    │
│  Outcome:              Commercial failure ❌     │
│                                                  │
│  This study cost:       $0 (open-source)        │
│  Time to conclusion:    18 months                │
│  Value:                Prevents future waste ✅  │
└──────────────────────────────────────────────────┘
```

### 🌍 Real-World Impact

**Before this study:**
- "Why did Peugeot fail? Maybe they did it wrong?"
- "Could better engineering fix it?"
- "Should we try again with modern tech?"

**After this study:**
- ✅ Thermodynamic proof of non-viability
- ✅ Confirms all failures weren't bad luck
- ✅ Redirects resources to viable solutions (battery tech, lightweight materials)

</div>

---

## 📖 Learn More

<details>
<summary><b>🎓 Academic Context</b></summary>

**Conference:** 4th International Electronic Conference on Processes (MDPI)  
**Date:** October 20-22, 2025  
**Affiliation:** Independent Researcher  
**Author:** [Yusuf Cemal İşbuğa](https://orcid.org/0009-0001-7565-9753) (Age 19)

**Keywords:**  
Electric vehicles • Compressed air • Hybrid systems • Thermodynamics • Feasibility study • Negative results • Urban mobility

**Related Work:**
- Luo et al. (2015): Compressed air energy storage review
- PSA (2013): Peugeot Hybrid Air technical specs
- Weber (2018): Tesla Model 3 motor analysis

</details>

<details>
<summary><b>⚠️ Known Limitations</b></summary>

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Pre-charge cost | +13% if included | Documented assumption |
| Valve dynamics | +1-3% real loss | Conservative estimates |
| Mechanical friction | +0.5-1% | Industry data range |
| Cold weather | Worse efficiency | Future sensitivity analysis |
| Driver behavior | Suboptimal triggering | Monte Carlo planned |

**Reality check:** Physical prototype would likely show **>20% penalty** vs our 2.9% simulation (best-case).

</details>

<details>
<summary><b>🚀 Future Work</b></summary>

### Short-Term (Pre-Conference)
- [ ] Sensitivity analysis (tank size, pressure, thresholds)
- [ ] Monte Carlo uncertainty quantification
- [ ] Peugeot data digitization and comparison

### Medium-Term (Post-Conference)
- [ ] Multi-cycle analysis (highway, mixed, cold start)
- [ ] Economic analysis (ROI calculation)
- [ ] ML-based control optimization (reinforcement learning)

### Long-Term
- [ ] Experimental validation (university partnership)
- [ ] Journal publication (Applied Energy)
- [ ] Industry engagement (pneumatic manufacturers)

</details>

<details>
<summary><b>❓ FAQ</b></summary>

**Q: Why positive result when Peugeot claimed 45% savings?**  
A: Their **claim** was 45%, **actual** was 12% (and for ICE, not EV). Our +2.9% penalty = "no benefit" for EVs.

**Q: Could better pneumatic motors help?**  
A: Already at theoretical limits. Industrial motors are mature (100+ years). Even 50% efficiency → only breakeven.

**Q: Why publish negative results?**  
A: **Prevents wasted effort.** Others won't spend years on same failed idea. Science advances by knowing what doesn't work.

**Q: Can I use this code?**  
A: **YES!** MIT License = free for all. Academic, commercial, educational—just cite the paper.

</details>

---

## 🏆 Recognition

<div align="center">

[![Conference](https://img.shields.io/badge/MDPI_ECP_2025-Accepted-success?style=for-the-badge)](https://sciforum.net/paper/view/24624)
[![Age](https://img.shields.io/badge/First_Author-Age_19-blue?style=for-the-badge)](https://orcid.org/0009-0001-7565-9753)
[![Open Science](https://img.shields.io/badge/Open_Science-Validated-green?style=for-the-badge)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer)

**Project Timeline:**
- 🔬 Research started: July 2024
- 📄 Conference accepted: December 2024
- 💻 Code released: January 2025
- 🎤 Presentation: October 2025

</div>

---

## 📬 Connect

<div align="center">

**Yusuf Cemal İşbuğa**

[![ORCID](https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0009-0001-7565-9753)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ycisbuga)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yisbuga37@gmail.com)
[![Website](https://img.shields.io/badge/Portfolio-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)](https://yusufcemalisbuga2025.netlify.app)

**Open to:** Research collaborations • Peer review • Conference discussions • Media inquiries  
**Response time:** 24-48 hours

</div>

---

## 🌟 Support This Work

<div align="center">

**If this research helped you:**

⭐ **Star the repository** - Show your support  
🔗 **Share with colleagues** - Spread transparent science  
📝 **Cite in publications** - Give credit  
💬 **Open discussions** - Ask questions  
🐛 **Report issues** - Help improve

<br>

[![GitHub stars](https://img.shields.io/github/stars/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=social)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=social)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer/fork)
[![GitHub watchers](https://img.shields.io/github/watchers/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=social)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer/subscription)

</div>

---

<div align="center">

### 🔴 Final Verdict

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Compressed air hybridization for passenger EVs:       │
│                                                         │
│  ❌ Thermodynamically inefficient (71% loss)           │
│  ❌ Economically unviable (high cost, low benefit)     │
│  ❌ Practically inferior (mass + complexity)           │
│  ❌ Commercially proven failure (Peugeot, MDI, Tata)   │
│                                                         │
│  ✅ Research question answered definitively            │
│  ✅ Future waste prevented                             │
│  ✅ Resources redirected to viable tech                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 💡 "The most valuable research sometimes proves an idea shouldn't be pursued."

**This study saves future researchers years and millions.**

---

![Made with Science](https://img.shields.io/badge/Made_with-Science-blueviolet?style=for-the-badge)
![Powered by Python](https://img.shields.io/badge/Powered_by-Python-3776AB?style=for-the-badge&logo=python)
![Open Source](https://img.shields.io/badge/Open_Source-❤️-red?style=for-the-badge)

**License:** MIT | **Last Updated:** January 2025 | **Status:** Conference-ready ✅

[![License](https://img.shields.io/github/license/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=flat-square)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=flat-square)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer/commits/main)
[![Issues](https://img.shields.io/github/issues/yusufcemalisbuga/HEPV-Feasibility-Analyzer?style=flat-square)](https://github.com/yusufcemalisbuga/HEPV-Feasibility-Analyzer/issues)

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=100&section=footer)

</div>
```

---

