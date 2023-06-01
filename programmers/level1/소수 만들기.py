from itertools import combinations


def isprime(n):
    prime = [False, False] + [True] * (n - 1)
    for i in range(len(prime)):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False
    return prime[n]


def solution(nums):
    answer = 0
    for combi in list(combinations(nums, 3)):
        if isprime(sum(combi)):
            answer += 1
    return answer
