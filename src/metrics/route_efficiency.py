def route_efficiency(distance_km: float) -> float:
    """
    Placeholder metric for route distance efficiency.
    Lower distance generally indicates better routing.

    Reject negative distances, which are invalid route telemetry.
    """
    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")
    return distance_km
