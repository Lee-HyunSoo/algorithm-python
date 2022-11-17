import sys


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


n, m = map(int, sys.stdin.readline().split())
high, low = gcd(n, m), 0
for i in range(1, 1000000001):
    if i % n == i % m == 0:
        low = i
        break
print(high, low)




