from dataclasses import dataclass


@dataclass
class ThermalController:
    """
    SG Thermal Controller

    Simple PID-like thermal control with:
    - target temperature
    - tolerance band
    - maximum safe temperature (emergency)
    - proportional/integral/derivative gains (simplified)

    Output:
    - cooling_level: 0.0 - 1.0 (fraction of maximum cooling)
    - emergency_flag: True if system is in dangerous zone
    """

    target_temp: float
    tolerance: float
    max_safe_temp: float
    kp: float = 0.03
    ki: float = 0.0
    kd: float = 0.01

    _integral_error: float = 0.0
    _last_error: float = 0.0
    _initialized: bool = False

    def compute_control_action(self, current_temp: float, dt: float = 1.0):
        """
        Compute cooling level and emergency state for a given temperature.
        dt is time step (seconds) between calls (for I/D components).
        """

        # Error relative to target
        error = current_temp - self.target_temp

        # Proportional term
        p_term = self.kp * error

        # Integral term
        self._integral_error += error * dt
        i_term = self.ki * self._integral_error

        # Derivative term
        if not self._initialized:
            d_term = 0.0
            self._initialized = True
        else:
            d_error = (error - self._last_error) / dt
            d_term = self.kd * d_error

        self._last_error = error

        # Raw cooling output (higher error => more cooling)
        raw_output = p_term + i_term + d_term

        # Map to [0.0, 1.0] range
        cooling_level = max(0.0, min(1.0, raw_output))

        # Introduce basic hysteresis using tolerance band:
        # if within tolerance, we nudge output toward gentler cooling.
        if abs(error) <= self.tolerance:
            cooling_level *= 0.5

        # Emergency if above max_safe_temp
        emergency_flag = current_temp >= self.max_safe_temp

        return cooling_level, emergency_flag
