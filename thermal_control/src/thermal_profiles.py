def get_thermal_profile(name: str) -> dict:
    """
    Return predefined thermal control profiles.

    Profiles:
    - 'silent'      : higher temps allowed, gentle cooling
    - 'balanced'    : moderate temps, balanced cooling
    - 'performance' : lower temps, aggressive cooling
    - 'safe'        : conservative, safety prioritized
    """
    profiles = {
        "silent": {
            "target_temp": 70.0,
            "tolerance": 5.0,
            "max_safe_temp": 85.0,
            "kp": 0.02,
            "ki": 0.0,
            "kd": 0.01,
        },
        "balanced": {
            "target_temp": 65.0,
            "tolerance": 3.0,
            "max_safe_temp": 80.0,
            "kp": 0.03,
            "ki": 0.001,
            "kd": 0.01,
        },
        "performance": {
            "target_temp": 60.0,
            "tolerance": 2.0,
            "max_safe_temp": 78.0,
            "kp": 0.05,
            "ki": 0.002,
            "kd": 0.02,
        },
        "safe": {
            "target_temp": 55.0,
            "tolerance": 2.0,
            "max_safe_temp": 70.0,
            "kp": 0.06,
            "ki": 0.003,
            "kd": 0.02,
        },
    }

    return profiles.get(name, profiles["balanced"])
