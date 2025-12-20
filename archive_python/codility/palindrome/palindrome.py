from collections import Counter

'''
3글자의 회문
같은 문자 2개(양 끝) = pair 1개가 꼭 필요함.
문자 총량은 회문 1개당 3글자가 필요함. 그러므로 최대 개수는 len(S) // 3 을 넘길 수 없다.
테스트 인수 중 'fknfkn' 케이스를 포함하기 위해..
결국 pair가 몇개인가 / 전체 글자수로 만들 수 있는 최대치 중에, 작은 값이 정답임.
'''


def solution(S):
    count = Counter(S)

    pairs = sum(c // 2 for c in count.values())
    return min(pairs, len(S) // 3)


print(solution("aaaabc"))
# 출력 : 2

print(solution("xyzwy"))
# 출력 : 1

print(solution("dd"))
# 출력 : 0

print(solution("fknfkn"))
# 출력 : 2
