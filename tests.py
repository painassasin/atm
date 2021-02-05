import unittest
from atm import ATM


class AtmTestCase(unittest.TestCase):
    def test_atm_get(self):
        atm = ATM()
        atm.put(100, 8)
        atm.put(500, 5)
        atm.put(1000, 4)
        self.assertEqual(atm.balance, 7300)

        self.assertDictEqual(atm.get(5200), {1000: 4, 500: 2, 100: 2})
        self.assertEqual(atm.balance, 2100)

        self.assertDictEqual(atm.get(1300), {500: 2, 100: 3})
        self.assertEqual(atm.balance, 800)

        self.assertIsNone(atm.get(1500))


if __name__ == '__main__':
    unittest.main()
