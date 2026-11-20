
import pytest
from src.wallet_withdrawal import withdraw


# Test 1: Valid withdrawal
def test_valid_withdrawal():
    assert withdraw(1000, 300) == 700


# Test 2: Withdraw exact balance
def test_withdraw_exact_balance():
    assert withdraw(1000, 1000) == 0


# Test 3: Zero withdrawal
def test_zero_withdrawal():
    with pytest.raises(ValueError):
        withdraw(1000, 0)


# Test 4: Negative withdrawal
def test_negative_withdrawal():
    with pytest.raises(ValueError):
        withdraw(1000, -100)


# Test 5: Withdrawal above balance
def test_withdrawal_above_balance():
    with pytest.raises(ValueError):
        withdraw(1000, 1200)


# Test 6: Negative balance
def test_negative_balance():
    with pytest.raises(ValueError):
        withdraw(-100, 50)


# Test 7: String input
def test_string_input():
    with pytest.raises(TypeError):
        withdraw("1000", 100)


# Test 8: Float input
def test_float_input():
    with pytest.raises(TypeError):
        withdraw(1000.5, 100)


# Test 9: Boolean input
def test_boolean_input():
    with pytest.raises(TypeError):
        withdraw(True, 100)
