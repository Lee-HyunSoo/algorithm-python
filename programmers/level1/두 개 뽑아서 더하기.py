from itertools import combinations


def solution(numbers):
    return sorted(list(set(sum(i) for i in list(combinations(numbers, 2)))))
