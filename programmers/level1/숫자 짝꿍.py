from collections import Counter


def solution(X, Y):
    X, Y = Counter(X), Counter(Y)

    answer = ''
    for key, value in X.items():
        if Y[key] != 0:
            for _ in range(min(value, Y[key])):
                answer += key
    if answer.count('0') == len(answer) and len(answer) != 0:
        answer = '0'

    return "".join(sorted(answer, reverse=True)) if len(answer) != 0 else '-1'
