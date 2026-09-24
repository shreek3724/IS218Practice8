from calculator.app import add, subtract


def test_add_positive_integers():
    """Verify standard addition handles baseline integers."""
    assert add(4, 5) == 9


def test_add_negative_integers():
    """Verify calculation engine correctly computes signed numbers."""
    assert add(-2, -8) == -10


def test_add_zero_identity():
    """Verify that adding zero returns the baseline value."""
    assert add(7, 0) == 7

# Keep your existing addition tests here...


def test_subtract_positive_result():
    """Verify standard baseline subtraction properties."""
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    """Verify system handles boundary transitions below zero."""
    assert subtract(3, 8) == -5


def test_subtract_zero_identity():
    """Verify subtracting zero yields the original value."""
    assert subtract(12, 0) == 12
