import sys
from collections import deque


def bfs(graph, visit, i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < len(graph) and 0 <= y + dy < len(graph[0]):
                if graph[x + dx][y + dy] == 1 and not visit[x + dx][y + dy]:
                    q.append((x + dx, y + dy))
                    visit[x + dx][y + dy] = True
    return 1


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * (n + 1) for _ in range(m + 1)]
    visit = [[False] * (n + 1) for _ in range(m + 1)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    answer = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if graph[i][j] == 1 and not visit[i][j]:
                answer += bfs(graph, visit, i, j)
    print(answer)
