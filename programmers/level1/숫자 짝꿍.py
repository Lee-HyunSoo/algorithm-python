from collections import Counter


def solution(X, Y):
    answer = ''
    X, Y = Counter(X), Counter(Y)

    for key, value in Counter(X).items():
        if Y[key] != 0:
            for i in range(min(value, Y[key])):
                answer += key
    if answer.count('0') == len(answer) and len(answer) != 0:
        answer = '0'

    return "".join(sorted(answer, reverse=True)) if len(answer) != 0 else '-1'
