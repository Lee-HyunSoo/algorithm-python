import sys


def dfs(graph, visit, x):
    visit[x] = True
    if True not in visit:
        return

    for y in range(len(graph[x])):
        if graph[x][y] == 1 and not visit[y]:
            dfs(graph, visit, y)


n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

answer = 0
for i in range(1, n + 1):
    if not visit[i]:
        dfs(graph, visit, i)
        answer += 1
print(answer)
