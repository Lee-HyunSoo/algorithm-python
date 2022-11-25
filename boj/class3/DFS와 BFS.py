import sys
from collections import deque


def bfs(graph, visit, v):
    q = deque()
    q.append(v)
    visit[v] = True
    print(v, end=' ')
    while q:
        x = q.popleft()

        for y in range(len(graph[x])):
            if graph[x][y] == 1 and not visit[y]:
                q.append(y)
                print(y, end=' ')
                visit[y] = True


def dfs(graph, visit, v, cnt):
    if cnt == len(graph) - 1:
        return

    print(v, end=' ')
    visit[v] = True
    for y in range(len(graph[v])):
        if graph[v][y] == 1 and not visit[y]:
            dfs(graph, visit, y, cnt + 1)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

visit = [False] * (n + 1)
dfs(graph, visit, v, 0)
print()
visit = [False] * (n + 1)
bfs(graph, visit, v)
