import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

q = deque()
visit = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))
            visit[i][j] = True

while q:
    x, y = q.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx < n and 0 <= y + dy < m:
            if tomato[x + dx][y + dy] == 0 and not visit[x + dx][y + dy]:
                tomato[x + dx][y + dy] = tomato[x][y] + 1
                visit[x + dx][y + dy] = True
                q.append((x + dx, y + dy))

answer = 0
for t in tomato:
    answer = max(answer, max(t))
    if 0 in t:
        print(-1)
        break
else:
    print(answer - 1)
