'''
길이가 N인 블록 배열 blocks가 주어진다.
각 블록에는 1 이상 50 이하의 색 번호가 지정되어 있다.
우리는 이 블록 중 최대 K개를 선택해 임의의 색상(1~50) 으로 다시 칠할 수 있다.

이때, 어떤 하나의 색상을 골라
그 색상으로 이루어진 가장 긴 연속 구간(덩어리) 의 길이를
최대로 만드는 것이 목표이다.

다시 말해:

블록 배열에서 단 하나의 색을 선택하고,
최대 K개의 블록을 그 색으로 바꿨을 때
만들 수 있는 가장 긴 연속된 구간의 길이를 구하라.

📝 입력 형식
	•	blocks: 길이 N의 정수 배열
	    •	각 원소는 1~50 사이의 정수
	    •	blocks[i]는 i번째 블록의 색을 나타냄
	•	K: 정수 (0 ≤ K ≤ N)
	    •	다시 칠할 수 있는 최대 블록 수

🎯 출력 형식
	•	한 색상에 대해 만들 수 있는 가장 긴 연속 구간의 최대 길이를 정수로 반환한다.
'''


def solution(blocks, K):
    N = len(blocks)
    colors = set(blocks)
    answer = 0

    for c in colors:
        left = 0
        changes = 0  # c로 바꿔야 하는 개수
        for right in range(N):
            if blocks[right] != c:
                changes += 1

            while changes > K:
                if blocks[left] != c:
                    changes -= 1
                left += 1

            # 현재 윈도우 [left, right]는 c로 만들 수 있는 구간
            answer = max(answer, right - left + 1)

    return answer


print(solution([1, 2, 1, 2, 1, 3, 3], 2))
