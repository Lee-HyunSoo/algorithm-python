import sys
n, m = map(int, sys.stdin.readline().split())
pocket = dict()
for i in range(1, n + 1):
    mon = sys.stdin.readline().strip()
    pocket[mon] = i
    pocket[str(i)] = mon

for _ in range(m):
    data = sys.stdin.readline().strip()
    print(pocket[data])
