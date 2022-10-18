from collections import deque


def check(s):
    stack = []
    for c in s:
        if c == ')':
            if not stack or stack[-1] != '(' or stack.count('(') == 0:
                return 0
            else:
                stack.pop(-1)
        elif c == '}':
            if not stack or stack[-1] != '{' or stack.count('{') == 0:
                return 0
            else:
                stack.pop(-1)
        elif c == ']':
            if not stack or stack[-1] != '[' or stack.count('[') == 0:
                return 0
            else:
                stack.pop(-1)
        else:
            stack.append(c)

    return 1 if not stack else 0


def solution(s):
    answer = 0
    s = deque(s)

    for _ in range(len(s)):
        answer += check(s)
        tmp = s.popleft()
        s.append(tmp)
    return answer

print(solution("[](){}"))


