def turn_accuracy(wrong_turns: int) -> int:
    """
    Number of wrong turns taken.
    Lower is better. Negative counts are invalid telemetry.
    """
    if wrong_turns < 0:
        raise ValueError("wrong_turns must be non-negative")
    return wrong_turns
