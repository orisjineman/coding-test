import unittest
import src_2525


class TestSolution(unittest.TestCase):
    def test_solution_10_10_10(self):
        hour = 10
        min = 10
        duration = 10

        result = src_2525.solution(hour, min, duration)

        self.assertEqual('10 20', result)

    def test_solution_0_30_90(self):
        hour = 0
        min = 30
        duration = 90
        result = src_2525.solution(hour, min, duration)

        self.assertEqual('2 0', result)

    def test_solution_23_45_90(self):
        hour = 23
        min = 45
        duration = 90
        result = src_2525.solution(hour, min, duration)

        self.assertEqual('1 15', result)

    def test_solution_23_30_30(self):
        hour = 23
        min = 30
        duration = 30
        result = src_2525.solution(hour, min, duration)

        self.assertEqual('0 0', result)


if __name__ == '__main__':
    unittest.main()
