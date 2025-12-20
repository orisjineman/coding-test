'''
팩토리얼
'''


# 반복문으로 구현한 n!
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


# 각각의 방식으로 구현한 n! 출력
print(factorial(5))
print(factorial_recursive(5))
