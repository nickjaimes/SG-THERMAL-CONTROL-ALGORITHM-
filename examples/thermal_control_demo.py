---

## 🔟 `examples/thermal_control_demo.py`

```python
"""
Simple simulation demo for SG Thermal Control Algorithm.

This simulates a device warming up and cooling down,
showing how the controller adjusts the cooling level.
"""

import random
import time

from thermal_control.src.thermal_controller import ThermalController
from thermal_control.src.thermal_profiles import get_thermal_profile


def main():
    profile = get_thermal_profile("balanced")
    controller = ThermalController(**profile)

    # Simulated temperature (start cool)
    temp = 40.0

    print("\n[SG THERMAL CONTROL DEMO] Profile: balanced\n")

    for step in range(1, 31):
        # Simulate workload causing heat (random)
        workload_factor = random.uniform(0.0, 1.0)
        temp += 0.6 * workload_factor  # device heating
        temp -= 0.3  # passive cooling effect

        cooling_level, emergency = controller.compute_control_action(temp)

        # cooling effect (the higher the cooling level, the more temp drops next tick)
        temp -= cooling_level * 0.8

        print(
            f"Step {step:02d} | Temp: {temp:5.2f}°C | Cooling: {cooling_level:4.2f} | "
            f"{'EMERGENCY' if emergency else ''}"
        )

        time.sleep(0.2)  # for human viewing

    print("\nDemo complete.\n")


if __name__ == "__main__":
    main()
