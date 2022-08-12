import pytest

from atm import ATM


@pytest.fixture
def new_atm() -> ATM:
    return ATM()
