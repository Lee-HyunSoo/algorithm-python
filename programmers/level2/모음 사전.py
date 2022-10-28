from itertools import product


def solution(word):
    dic, answer = 'AEIOU', set()
    for i in range(1, 6):
        for c in list(product(dic, repeat=i)):
            answer.add(''.join(c))

    for i, w in enumerate(sorted(answer)):
        if w == word:
            return i + 1
