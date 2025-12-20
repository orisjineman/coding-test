"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.

예제 입력
5
1 1
2 3
3 4
9 8
5 2

예제 출력
2
5
7
17
7
"""


def solution(left, right) -> int:
    if not (0 < left and right < 10):
        raise Exception('Invalid argument')

    return left + right


def run(repeat_cnt):
    for i in range(0, repeat_cnt):
        left, right = tuple(input().split(' '))
        left, right = int(left), int(right)
        
        result = solution(left, right)
        print(result)


if __name__ == '__main__':
    arg = input()
    repeat_cnt = int(arg)
    run(repeat_cnt)
