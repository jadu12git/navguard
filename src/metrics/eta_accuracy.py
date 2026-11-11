import math


def eta_error_percentage(eta_seconds: float, actual_seconds: float) -> float:
    """
    Computes absolute ETA error percentage.
    Lower is better.

    Raises ValueError when the predicted ETA is not positive, since a
    percentage error cannot be calculated with a zero or negative baseline.
    """
    if not math.isfinite(eta_seconds) or eta_seconds <= 0:
        raise ValueError("eta_seconds must be positive")
    return abs(actual_seconds - eta_seconds) / eta_seconds
