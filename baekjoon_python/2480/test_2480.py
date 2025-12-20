import unittest
import src_2480

"""
1에서부터 6까지의 눈을 가진 3개의 주사위

예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
"""


class TestSolution(unittest.TestCase):
    def test_when_all_pips_are_equal(self):
        a, b, c = 2, 2, 2

        result = src_2480.solution(a, b, c)

        self.assertEqual(12000, result)

    def test_when_all_pips_are_different(self):
        a, b, c = 6, 2, 5

        result = src_2480.solution(a, b, c)

        self.assertEqual(600, result)

    def test_when_2_pips_are_equal1(self):
        a, b, c = 3, 3, 6

        result = src_2480.solution(a, b, c)

        self.assertEqual(1300, result)

    def test_when_2_pips_are_equal2(self):
        a, b, c = 3, 6, 3

        result = src_2480.solution(a, b, c)

        self.assertEqual(1300, result)

    def test_when_2_pips_are_equal3(self):
        a, b, c = 6, 3, 3

        result = src_2480.solution(a, b, c)

        self.assertEqual(1300, result)


if __name__ == '__main__':
    unittest.main()
