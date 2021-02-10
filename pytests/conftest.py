from pytest import fixture
from atm import ATM


@fixture
def new_atm() -> ATM:
    atm = ATM()
    return atm
