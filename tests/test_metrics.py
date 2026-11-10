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
