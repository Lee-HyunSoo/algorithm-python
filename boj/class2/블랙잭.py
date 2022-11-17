import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
bj = list(combinations(sys.stdin.readline().split(), 3))
tmp = []
for b in bj:
    total = 0
    for data in b:
        total += int(data)
    tmp.append(total)

answer = 0
for t in tmp:
    if t <= m:
        answer = max(answer, t)
print(answer)

