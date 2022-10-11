from collections import defaultdict

def solution(survey, choices):
    checks = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    score = defaultdict(int)
    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += 4 - c
        else:
            score[s[1]] += c - 4

    answer = ''
    for check in checks:
        if score[check[0]] < score[check[1]]:
            answer += check[1]
        else:
            answer += check[0]

    return answer

print(solution(["TR", "RT", "TR"], [7, 1, 3]))
