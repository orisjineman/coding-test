import unittest
from src_25304 import solution


class TestSolution(unittest.TestCase):
    def test_receipt_yes(self):
        total_price = 260000
        good_list = [(20000, 5), (30000, 2), (10000, 6), (5000, 8)]
        result = solution(total_price, good_list)
        self.assertEqual('Yes', result)

    def test_receipt_no(self):
        total_price = 250000
        good_list = [(20000, 5), (30000, 2), (10000, 6), (5000, 8)]
        result = solution(total_price, good_list)
        self.assertEqual('No', result)


if __name__ == '__main__':
    unittest.main()
