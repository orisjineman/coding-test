import unittest
from src_2739 import solution


class TestSolution(unittest.TestCase):
    def test_when_times_table_num_is_0(self):
        with self.assertRaises(Exception):
            times_table_num = 0
            result = solution(times_table_num)
            print(result)

    def test_when_times_table_num_is_10(self):
        with self.assertRaises(Exception):
            times_table_num = 10
            result = solution(times_table_num)
            print(result)

    def test_when_times_table_num_is_2(self):
        times_table_num = 2
        result = solution(times_table_num)
        expected = f'''2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18'''
        self.assertEqual(expected, result)

    def test_when_times_table_num_is_7(self):
        times_table_num = 7
        result = solution(times_table_num)
        expected = f'''7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63'''
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
