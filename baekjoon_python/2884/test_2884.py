import unittest
import src_2884


class TestSolution(unittest.TestCase):
    def test_solution_10_10(self):
        hour = 10
        min = 10
        result = src_2884.solution(hour, min)

        self.assertEqual(result, '9 25')

    def test_solution_0_30(self):
        hour = 0
        min = 30
        result = src_2884.solution(hour, min)

        self.assertEqual(result, '23 45')

    def test_solution_23_40(self):
        hour = 23
        min = 40
        result = src_2884.solution(hour, min)

        self.assertEqual(result, '22 55')

    def test_solution_0_0(self):
        hour = 0
        min = 0
        result = src_2884.solution(hour, min)

        self.assertEqual(result, '23 15')

    def test_solution_0_45(self):
        # 경계값 테스트 추가 -> 24 0 이 아닌, 0 0 이 나와야 한다.
        hour = 0
        min = 45
        result = src_2884.solution(hour, min)

        self.assertEqual(result, '0 0')


if __name__ == '__main__':
    unittest.main()
