def solution(s):
    s = list(reversed(s))
    word = []
    while len(s) > 0:
        tmp = s.pop()
        if tmp == '(':
            word.append(tmp)
        elif tmp == ')':
            if not word:
                return False
            word.pop()
    return False if word else True

