# 🌡 THERMAL CONTROL DESIGN  
**SG Thermal Control Algorithm – Design Overview**

---

## 🎯 Goal

Provide a **simple but robust thermal control algorithm** that:

- Keeps temperature near a **target value**
- Respects a **safe maximum temperature**
- Avoids excessive oscillation (via tolerance band & PID terms)
- Can be tuned per device/environment profile

---

## 🧠 Control Model

We use a simple **PID-like scheme**:

- **P (Proportional)** – reacts to how far we are from target temperature  
- **I (Integral)** – accumulates long-term bias (optionally used)  
- **D (Derivative)** – reacts to how fast temperature is changing  

Output → `cooling_level` between `0.0 – 1.0`  
(0.0 = no cooling, 1.0 = maximum cooling)

If `current_temp >= max_safe_temp` → `emergency_flag = True`.

---

## 🔧 Hysteresis & Tolerance

To avoid rapid fan/actuator toggling, we use a **tolerance band**:

- If `abs(current_temp - target_temp) <= tolerance`  
  → we **reduce cooling intensity** to avoid oscillation

Example:
- Target = 65°C  
- Tolerance = 3°C  
- Temps between 62–68°C considered “OK band”

---

## 🧬 Profiles

Profiles define:

- `target_temp`
- `tolerance`
- `max_safe_temp`
- PID gains (`kp`, `ki`, `kd`)

Profiles (example set):

- `silent`  
- `balanced`  
- `performance`  
- `safe`  

These can be extended per hardware class (laptops, servers, pods).

---

## ⚠ Safety

If `emergency_flag` is True:

- Upstream logic (SG OS, TRINITY, hardware controller) may:
  - Force maximum cooling  
  - Reduce performance (throttle CPU/GPU)  
  - In extreme case: initiate controlled shutdown  

---

## 🔗 SG Integration

Thermal control is **not isolated** – it is part of the SG health:

- TRINITY AI:
  - Monitors thermal behavior
  - Adjusts profile (silent ↔ performance) as needed
  - Logs thermal anomalies into QNSF

- EAGLE EYE:
  - Treats abnormal heat as **risk signal**
  - Correlates with workload & external environment (e.g., heatwave)

- QNSF:
  - Learns:
    - Seasonal patterns
    - Device ageing trends
    - Best profiles for different conditions

---

## 🖋 Author

Designed by **Nicolas E. Santiago**  
Safeway Guardian – Saitama, Japan – 2025  
Powered by **ChatGPT**
