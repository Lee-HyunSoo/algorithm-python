import math


def convert(n, base):
    T = "0123456789"
    q, r = divmod(n, base)  # 몫, 나머지
    return convert(q, base) + T[r] if q else T[r]


def isprime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True


def solution(n, k):
    answer = 0
    num = convert(n, k).split('0')

    for n in num:
        if n.isnumeric() and isprime(int(n)):
            answer += 1
    return answer

print(solution(11000011, 10))