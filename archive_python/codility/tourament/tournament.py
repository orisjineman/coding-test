def solution(skills):  # skills의 각 인덱스는 선수 번호와 동일함 !
    n = len(skills)
    results = [0] * n
    round_num = 1  # 시작 라운드 : 1

    # 현재 선수 인덱스를 담고 있는 리스트
    current = list(range(n))

    while len(current) > 1:  # 탈락할때마다 삭제하는 아이디어
        next_round = []  # 현재 라운드가 종료되고 나면, 다음 라운드에 진출할 선수번호가 담길 것이다.

        # 현재 라운드 시작
        for i in range(0, len(current), 2):  # 2명씩 대결
            left = current[i]
            right = current[i + 1]

            # 경기
            if skills[left] > skills[right]:  # 오른쪽 선수가 패배한 경우
                results[right] = round_num  # 오른쪽 선수의 인덱스 위치에, 현재 round_num 넣음
                next_round.append(left)  # 왼쪽 선수는 다음 라운드 진출 !!!
            else:  # 왼쪽 선수가 패배한 경우, 상기와 반대로 진행
                results[left] = round_num
                next_round.append(right)

        current = next_round  # 현재 라운드 종료되었으니, 다음 라운드 진출 선수 목록을 current에 넣고 다음 반복으로 ㄱㄱ
        round_num += 1  # 다음 라운드 number

    # 마지막 우승자 라운드는 -1 해줘야함
    results[current[0]] = round_num - 1
    return results

print(solution([4, 2, 7, 3, 1, 8, 6, 5]))
'''
출력
[2, 1, 3, 1, 1, 3, 2, 1]
'''

print(solution([4, 2, 1, 3]))
'''
출력
[2, 1, 1, 2]
'''

print(solution([3, 4, 2, 1]))
'''
출력
[1, 2, 2, 1]
'''