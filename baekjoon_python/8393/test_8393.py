import unittest
from src_8393 import solution


class TestSolution(unittest.TestCase):
    def test_addition_0(self):
        # 경계값
        with self.assertRaises(Exception):
            number = 0
            solution(number)

    def test_addition_10001(self):
        # 경계값
        with self.assertRaises(Exception):
            number = 10001
            solution(number)

    def test_addition_3(self):
        number = 3
        result = solution(number)
        self.assertEqual(6, result)

    def test_addition_10(self):
        number = 10
        result = solution(number)
        self.assertEqual(55, result)


if __name__ == '__main__':
    unittest.main()
