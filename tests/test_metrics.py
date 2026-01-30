from src.metrics.eta_accuracy import eta_error_percentage

def test_eta_accuracy():
    error = eta_error_percentage(100, 110)
    assert error == 0.10
