import sys

m, n = map(int, sys.stdin.readline().split())

prime = [False, False] + [True] * (n + 1)
for i in range(len(prime)):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

for i in range(m, n + 1):
    if prime[i]:
        print(i)
