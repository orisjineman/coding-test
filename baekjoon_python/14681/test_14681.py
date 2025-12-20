import unittest
import src_14681


class TestSolution(unittest.TestCase):
    def test_solution_0_0(self):
        x = 0
        y = 0
        result = src_14681.solution(x, y)

        self.assertEqual(result, 0)

    def test_solution_quadrant_1(self):
        x = 1
        y = 1
        result = src_14681.solution(x, y)

        self.assertEqual(result, 1)

    def test_solution_quadrant_2(self):
        x = -1
        y = 1
        result = src_14681.solution(x, y)

        self.assertEqual(result, 2)

    def test_solution_quadrant_3(self):
        x = -1
        y = -1
        result = src_14681.solution(x, y)

        self.assertEqual(result, 3)

    def test_solution_quadrant_4(self):
        x = 1
        y = -1
        result = src_14681.solution(x, y)

        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
