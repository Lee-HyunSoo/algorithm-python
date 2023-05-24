from itertools import combinations


def solution(number):
    answer = 0
    numbers = list(combinations(number, 3))
    for n in numbers:
        if sum(n) == 0:
            answer += 1
    return answer
