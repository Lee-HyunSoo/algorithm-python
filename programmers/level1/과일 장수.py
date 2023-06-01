def solution(k, m, score):
    score.sort(reverse=True)
    apples = [score[m * i: m * (i + 1)] for i in range(len(score) // m)]
    return sum(min(a) * m for a in apples)
