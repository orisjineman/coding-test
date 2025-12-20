'''
큰 수의 법칙
순서대로 2,4,5,4,6 으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6+6+6+5+6+6+6+5 인 46이 된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 ㅂ버칙에 따른 결과를 출력하시오.
'''

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

'''
입력
5 8 3
2 4 5 4 6

답
46
'''
