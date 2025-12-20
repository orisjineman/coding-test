def solution(x, y) -> int:
    result_val = 0

    if x == 0 and y == 0:
        result_val = 0
    elif x > 0 and y > 0:
        result_val = 1
    elif x < 0 and y > 0:
        result_val = 2
    elif x < 0 and y < 0:
        result_val = 3
    elif x > 0 and y < 0:
        result_val = 4

    return result_val


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    result = solution(x, y)
    print(result)
