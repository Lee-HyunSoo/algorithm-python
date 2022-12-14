import sys
from collections import deque


def bfs(picture, visit, n, i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    color = picture[i][j]

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if picture[x + dx][y + dy] == color and not visit[x + dx][y + dy]:
                    q.append((x + dx, y + dy))
                    visit[x + dx][y + dy] = True


n = int(sys.stdin.readline())
picture = []
for _ in range(n):
    picture.append(list(sys.stdin.readline().strip()))

answer1, answer2 = 0, 0
visit = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            answer1 += 1
            bfs(picture, visit, n, i, j)

for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

visit = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            answer2 += 1
            bfs(picture, visit, n, i, j)
print(answer1, answer2)
