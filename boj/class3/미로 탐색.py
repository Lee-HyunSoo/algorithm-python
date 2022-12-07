import sys
from collections import deque


def bfs(graph, n, m):
    q = deque()
    visit = [[False] * m for _ in range(n)]
    q.append((0, 0))
    visit[0][0] = True
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return graph[x][y]

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if graph[x + dx][y + dy] != 0 and not visit[x + dx][y + dy]:
                    graph[x + dx][y + dy] = graph[x][y] + 1
                    q.append((x + dx, y + dy))
                    visit[x + dx][y + dy] = True


n, m = map(int, sys.stdin.readline().split())
graph = [[0] * m for _ in range(n)]
for i in range(n):
    data = sys.stdin.readline().strip()
    for j in range(len(data)):
        graph[i][j] = int(data[j])
print(bfs(graph, n, m))
