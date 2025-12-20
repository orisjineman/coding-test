import unittest
from src_25314 import solution


class TestSolution(unittest.TestCase):
    def test_4(self):
        result = solution(4)
        self.assertEqual('long int', result)

    def test_20(self):
        result = solution(20)
        self.assertEqual('long long long long long int', result)


if __name__ == '__main__':
    unittest.main()
