def solution(n):
    answer = 1
    while n != 1:
        if n % 2 != 0:
            n -= 1
            answer += 1
        n //= 2
    return answer
