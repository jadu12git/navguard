from src.metrics.eta_accuracy import eta_error_percentage
from src.metrics.turn_accuracy import turn_accuracy
from src.metrics.route_efficiency import route_efficiency

def test_eta_accuracy():
    error = eta_error_percentage(100, 110)
    assert error == 0.10


def test_eta_accuracy_rejects_zero_baseline():
    import pytest

    with pytest.raises(ValueError, match="eta_seconds must be positive"):
        eta_error_percentage(0, 110)


def test_eta_accuracy_rejects_negative_baseline():
    import pytest

    with pytest.raises(ValueError, match="eta_seconds must be positive"):
        eta_error_percentage(-100, 110)


def test_eta_accuracy_rejects_nonfinite_baselines():
    import pytest

    for eta in (float("nan"), float("inf"), float("-inf")):
        with pytest.raises(ValueError, match="eta_seconds must be positive"):
            eta_error_percentage(eta, 110)


def test_eta_accuracy_rejects_invalid_actual_durations():
    import pytest

    for actual in (float("nan"), float("inf"), float("-inf"), -1):
        with pytest.raises(ValueError, match="actual_seconds must be finite and non-negative"):
            eta_error_percentage(100, actual)


def test_eta_accuracy_accepts_zero_actual_duration():
    # A zero actual time is mathematically valid, unlike a zero ETA baseline.
    assert eta_error_percentage(100, 0) == 1.0


def test_turn_accuracy_rejects_negative_counts():
    import pytest

    with pytest.raises(ValueError, match="wrong_turns must be non-negative"):
        turn_accuracy(-1)


def test_turn_accuracy_accepts_zero_and_positive_counts():
    assert turn_accuracy(0) == 0
    assert turn_accuracy(3) == 3


def test_route_efficiency_rejects_negative_distance():
    import pytest

    with pytest.raises(ValueError, match="distance_km must be non-negative"):
        route_efficiency(-0.1)


def test_route_efficiency_accepts_zero_and_positive_distance():
    assert route_efficiency(0) == 0
    assert route_efficiency(12.5) == 12.5
