

class ATM:
    BILLS = dict.fromkeys([10, 50, 100, 200, 500, 1000, 2000, 5000], 0)

    def __init__(self):
        self.balance = 0

    def put(self, bill, count):
        if bill in self.BILLS:
            self.BILLS[bill] += count
            self.balance += bill * count

    def get(self, amount) -> dict:
        result_bills = dict()
        values = list(self.BILLS.keys())
        values.sort(reverse=True)
        for value in values:
            count = amount // value
            num = count if count <= self.BILLS[value] else self.BILLS[value]
            amount -= num * value
            if num:
                result_bills[value] = num

        if not amount:
            for k, v in result_bills.items():
                self.BILLS[k] -= v
            self.balance -= sum([k*v for k, v in result_bills.items()])
            return result_bills

        print('Not enough money in ATM')
