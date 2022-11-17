import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k, n = int(sys.stdin.readline()), int(sys.stdin.readline())
    house = [i for i in range(1, n + 1)]
    tmp, total = [], 0
    for _ in range(k):
        for i in range(1, n):
            house[i] += house[i - 1]
    print(house[n - 1])
