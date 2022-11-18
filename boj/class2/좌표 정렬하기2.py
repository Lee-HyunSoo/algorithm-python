import sys

n = int(sys.stdin.readline())
coordinate = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))
coordinate.sort(key=lambda x: (x[1], x[0]))

for c in coordinate:
    print(c[0], c[1])
