import pytest

from exceptions import NotEnoughMoney


class TestATM:

    def test_success(self, new_atm):
        new_atm.put(100, 8)
        new_atm.put(500, 5)
        new_atm.put(1000, 4)
        assert new_atm.balance == 7300

        assert new_atm.get(5200) == {1000: 4, 500: 2, 100: 2}
        assert new_atm.balance == 2100

        assert new_atm.get(1300) == {500: 2, 100: 3}
        assert new_atm.balance == 800

    def test_not_enough_money(self, new_atm):
        new_atm.put(100, 1)
        with pytest.raises(NotEnoughMoney):
            new_atm.get(200)
