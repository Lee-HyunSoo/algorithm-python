import sys
from collections import deque


def bfs(graph, visit, i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if graph[x + dx][y + dy] == 1 and not visit[x + dx][y + dy]:
                    cnt += 1
                    q.append((x + dx, y + dy))
                    visit[x + dx][y + dy] = True
    return cnt


n = int(sys.stdin.readline())
graph = []
visit = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

total = 0
houses = []
for x in range(len(graph)):
    for y in range(len(graph[x])):
        if graph[x][y] == 1 and not visit[x][y]:
            total += 1
            houses.append(bfs(graph, visit, x, y))
print(total)
for h in sorted(houses):
    print(h)
