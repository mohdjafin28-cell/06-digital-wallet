
import pytest
from src.wallet_affordability import can_afford


# Test 1: Affordable purchase
def test_can_afford():
    assert can_afford(1000, 500) is True


# Test 2: Exact balance siva
def test_exact_balance():
    assert can_afford(1000, 1000) is True


# Test 3: Unaffordable purchase
def test_cannot_afford():
    assert can_afford(500, 1000) is False


# Test 4: Zero price
def test_zero_price():
    assert can_afford(0, 0) is True


# Test 5: Negative balance
def test_negative_balance():
    with pytest.raises(ValueError):
        can_afford(-100, 50)


# Test 6: Negative price
def test_negative_price():
    with pytest.raises(ValueError):
        can_afford(1000, -50)


# Test 7: String input
def test_string_input():
    with pytest.raises(TypeError):
        can_afford("1000", 500)


# Test 8: Float input
def test_float_input():
    with pytest.raises(TypeError):
        can_afford(1000.5, 500)


# Test 9: Boolean input
def test_boolean_input():
    with pytest.raises(TypeError):
        can_afford(True, 500)
