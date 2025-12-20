"""
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

입력
첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

출력
첫째 줄에 게임의 상금을 출력 한다.
"""


def solution(dice_pip_1, dice_pip_2, dice_pip_3) -> int:
    pips = [dice_pip_1, dice_pip_2, dice_pip_3]

    equal_cnt = []
    for idx in range(0, len(pips)):
        cnt = pips.count(pips[idx])
        equal_cnt.append(cnt)

    max_number_of_cnt = max(equal_cnt)
    return_val = 0
    if max_number_of_cnt == 3:
        target_number = pips[equal_cnt.index(max_number_of_cnt)]
        return_val = 10_000 + target_number * 1_000
    elif max_number_of_cnt == 2:
        target_number = pips[equal_cnt.index(max_number_of_cnt)]
        return_val = 1_000 + target_number * 100
    elif max_number_of_cnt == 1:
        target_numer = max(pips)
        return_val = target_numer * 100
    else:
        raise Exception('Unexpected results')

    return return_val


if __name__ == '__main__':
    arg = input()

    a, b, c = tuple(arg.split(' '))
    a = int(a)
    b = int(b)
    c = int(c)

    result = solution(a, b, c)
    print(result)
