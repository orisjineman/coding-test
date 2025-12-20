'''
숫자 카드 게임
가장 높은 숫자가 쓰인 카드 한 장을 뽑기
N x M 숫자 카드 (N: 행, M: 열)

먼저 뽑고자 하는 카드가 포함되어 있는 행 선택
그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드 뽑아야 함

따라서 처음에 카드를 골라낼 행을 선택할 때,
이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
'''
# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

'''
입력
3 3
3 1 2
4 1 4
2 2 2

출력
2
'''