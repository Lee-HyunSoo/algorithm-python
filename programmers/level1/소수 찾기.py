def solution(n):
    answer = 0
    prime = [False, False] + [True] * (n - 1)

    for i in range(len(prime)):
        if prime[i]:
            answer += 1
            for j in range(i * 2, n + 1, i):
                prime[j] = False
    return answer
