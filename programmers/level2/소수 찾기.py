from itertools import permutations


def solution(numbers):
    answer = set()
    numbers = list(map(str, numbers))
    for i in range(1, len(numbers) + 1):
        strnum = list(permutations(numbers, i))
        for s in strnum:
            snum = ''.join(s)
            if isprime(int(snum)):
                answer.add(int(snum))
    return len(answer)


def isprime(n):
    if n < 2:
        return 0

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        return 1


print(solution("011"))