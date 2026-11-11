from src.metrics.eta_accuracy import eta_error_percentage

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
