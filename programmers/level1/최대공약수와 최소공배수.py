def gcd(n, m):
    mod = n % m
    if mod != 0:
        n, m = m, mod
        return gcd(n, m)
    else:
        return m

def solution(n, m):
    return [gcd(n, m), int(n * m / gcd(n, m))]

