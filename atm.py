import logging

from exceptions import NotEnoughMoney

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ATM:

    def __init__(self):
        self.balance: int = 0
        self.bills: dict = dict.fromkeys((10, 50, 100, 200, 500, 1000, 2000, 5000), 0)

    def put(self, bill, count):
        """
        Кладет купюры `bill` в банкомат, в количестве `count`.
        :param bill:
        :param count:
        :return:
        """
        if bill in self.bills:
            self.bills[bill] += count
            self.balance += bill * count

    def get(self, amount) -> dict:
        """
        Выдает сумму `amount` из банкомата. В случае отсутствия нужной суммы
        вернет `None` и соответствующее сообщение.
        :param amount:
        :return:
        """
        result_bills = dict()
        for value in reversed(self.bills.keys()):
            count = amount // value
            num = count if count <= self.bills[value] else self.bills[value]
            amount -= num * value
            if num:
                result_bills[value] = num

        if not amount:
            for k, v in result_bills.items():
                self.bills[k] -= v
            self.balance -= sum([k * v for k, v in result_bills.items()])
            return result_bills

        logger.error('Not enough money in ATM')
        raise NotEnoughMoney
