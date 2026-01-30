def eta_error_percentage(eta_seconds: float, actual_seconds: float) -> float:
    """
    Computes absolute ETA error percentage.
    Lower is better.
    """
    return abs(actual_seconds - eta_seconds) / eta_seconds
