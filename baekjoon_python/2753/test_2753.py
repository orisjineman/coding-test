import unittest
import src_2753


class TestSolution(unittest.TestCase):
    def test_solution_0_invalid(self):
        arg = 0
        result = src_2753.solution(arg)
        self.assertEqual(result, 999)

    def test_solution_2012_is_leap_year(self):
        arg = 2012
        result = src_2753.solution(arg)
        self.assertEqual(result, 1)

    def test_solution_1900_is_not_leap_year(self):
        arg = 1900
        result = src_2753.solution(arg)
        self.assertEqual(result, 0)

    def test_solution_2000_is_leap_year(self):
        arg = 2000
        result = src_2753.solution(arg)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
