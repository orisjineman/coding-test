import unittest
from src_10950 import solution


class TestSolution(unittest.TestCase):
    def test_addition_0_9(self):
        # 경계값
        with self.assertRaises(Exception):
            left = 0
            right = 9
            solution(left, right)

    def test_addition_2_11(self):
        # 경계값
        with self.assertRaises(Exception):
            left = 2
            right = 11
            solution(left, right)

    def test_addition_1_9(self):
        left = 1
        right = 9
        result = solution(left, right)
        self.assertEqual(10, result)

    def test_addition_8_7(self):
        left = 8
        right = 7
        result = solution(left, right)
        self.assertEqual(15, result)


if __name__ == '__main__':
    unittest.main()
