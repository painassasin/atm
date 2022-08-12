import pytest

from exceptions import NotEnoughMoney, UnsupportedBill


def test_get_money_success(new_atm):
    new_atm.put(100, 8)
    new_atm.put(500, 5)
    new_atm.put(1000, 4)
    assert new_atm.balance == 7300

    assert new_atm.get(5200) == {1000: 4, 500: 2, 100: 2}
    assert new_atm.balance == 2100

    assert new_atm.get(1300) == {500: 2, 100: 3}
    assert new_atm.balance == 800


def test_not_enough_money(new_atm):
    new_atm.put(100, 1)
    with pytest.raises(NotEnoughMoney):
        new_atm.get(200)


def test_put_money(new_atm):
    new_atm.put(100, 2)
    assert new_atm.balance == 200
    new_atm.put(500, 3)
    assert new_atm.balance == 1700


def test_unsupported_bill(new_atm):
    with pytest.raises(UnsupportedBill):
        new_atm.put(-100, 1)
