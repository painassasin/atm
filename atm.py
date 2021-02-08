

class ATM:

    def __init__(self):
        self.balance = 0
        self.bills = dict.fromkeys((10, 50, 100, 200, 500, 1000, 2000, 5000), 0)

    def put(self, bill, count):
        if bill in self.bills:
            self.bills[bill] += count
            self.balance += bill * count

    def get(self, amount) -> dict:
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
            self.balance -= sum([k*v for k, v in result_bills.items()])
            return result_bills

        print('Not enough money in ATM')
