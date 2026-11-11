import math


def eta_error_percentage(eta_seconds: float, actual_seconds: float) -> float:
    """
    Computes absolute ETA error percentage.
    Lower is better.

    Raises ValueError when the predicted ETA is not positive, since a
    percentage error cannot be calculated with a zero or negative baseline.
    Raises ValueError for non-finite or negative actual travel times as well.
    """
    if not math.isfinite(eta_seconds) or eta_seconds <= 0:
        raise ValueError("eta_seconds must be positive")
    if not math.isfinite(actual_seconds) or actual_seconds < 0:
        raise ValueError("actual_seconds must be finite and non-negative")
    return abs(actual_seconds - eta_seconds) / eta_seconds
