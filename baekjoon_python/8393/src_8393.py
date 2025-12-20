"""
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
"""


def solution(number) -> int:
    if not (1 <= number <= 10000):
        raise Exception('Invalid argument')

    return_val = 0
    for i in range(1, number + 1):
        return_val += i

    return return_val


if __name__ == '__main__':
    arg = input()
    number = int(arg)
    print(solution(number))
