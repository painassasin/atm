import logging

from atm.exceptions import NotEnoughMoney, UnsupportedBill

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ATM:
    supported_bills = (10, 50, 100, 200, 500, 1000, 2000, 5000)

    def __init__(self):
        self._balance: int = 0
        self._bills: dict[int, int] = dict.fromkeys(self.supported_bills, 0)

    @property
    def balance(self) -> int:
        return self._balance

    def put(self, bill: int, count: int) -> None:
        """
        Кладет купюры `bill` в банкомат, в количестве `count`.
        """
        if bill not in self._bills:
            logger.error(f'Unsupported bill {bill}')
            raise UnsupportedBill

        self._bills[bill] += count
        self._balance += bill * count
        logger.info(f'Banknotes credited: bill={bill}, count={count}, balance={self._balance}')

    def get(self, amount: int) -> dict:
        """
        Выдает сумму `amount` из банкомата. В случае отсутствия нужной суммы
        выкинет исключение `NotEnoughMoney` и соответствующее сообщение.
        """
        result_bills = dict()
        for value in reversed(self._bills.keys()):
            count: int = amount // value
            num: int = count if count <= self._bills[value] else self._bills[value]
            amount -= num * value
            if num:
                result_bills[value] = num

        if not amount:
            for k, v in result_bills.items():
                self._bills[k] -= v
            self._balance -= sum([k * v for k, v in result_bills.items()])
            return result_bills

        logger.error('Not enough money in ATM')
        raise NotEnoughMoney
