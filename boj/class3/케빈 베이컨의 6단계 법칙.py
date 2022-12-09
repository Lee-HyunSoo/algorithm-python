import sys
from collections import deque


def bfs(graph, start, n):
    num = [0] * (n + 1)
    q = deque()
    q.append(start)
    visit = [start]

    while q:
        tmp = q.popleft()
        for g in graph[tmp]:
            if g not in visit:
                num[g] = num[tmp] + 1
                q.append(g)
                visit.append(g)
    return sum(num)


n, m = map(int, sys.stdin.readline().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

answer = []
for i in range(1, n + 1):
    answer.append(bfs(graph, i, n))
print(answer.index(min(answer)) + 1)
