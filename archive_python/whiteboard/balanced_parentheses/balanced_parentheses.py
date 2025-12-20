'''
괄호 짝 맞추기 문제
프로그래머스 Lv.1 수준이라고 한다...

입/출력값 예시
'(gi)'  -> True
'[ddd[' -> False
'[()]'  -> True
'[(]'   -> False
'''


def is_valid_brackets(s: str) -> bool:
    pair = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for ch in s:
        if ch in '([{':  # 여는 괄호
            stack.append(ch)
        elif ch in ')]}':  # 닫는 괄호
            if not stack:  # 닫는 게 먼저 나오면 실패
                return False
            if stack[-1] != pair[ch]:  # 짝이 안 맞으면 실패
                return False
            stack.pop()
        else:
            # 괄호 외 문자가 들어올 수도 있으면 무시/처리 정책 결정
            # 보통 문제에선 괄호만 온다고 가정
            pass

    return len(stack) == 0


print(is_valid_brackets('(gi)'))  # True
print(is_valid_brackets('[ddd['))  # False
print(is_valid_brackets('[()]'))  # True
print(is_valid_brackets('(])'))  # False
