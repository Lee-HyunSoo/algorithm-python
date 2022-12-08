import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque()
visit = [0] * 100001
q.append(n)

while q:
    pos = q.popleft()
    if pos == k:
        print(visit[pos])
        break

    for i in [pos + 1, pos - 1, pos * 2]:
        if 0 <= i <= 100000 and not visit[i]:
            q.append(i)
            visit[i] = visit[pos] + 1
