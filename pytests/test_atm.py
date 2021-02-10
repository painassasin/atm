def test_atm(new_atm):
    new_atm.put(100, 8)
    new_atm.put(500, 5)
    new_atm.put(1000, 4)
    assert new_atm.balance == 7300

    assert new_atm.get(5200) == {1000: 4, 500: 2, 100: 2}
    assert new_atm.balance == 2100

    assert new_atm.get(1300) == {500: 2, 100: 3}
    assert new_atm.balance == 800

    assert new_atm.get(1500) is None
