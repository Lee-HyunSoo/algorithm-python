import sys
from collections import deque

c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

graph = [[0] * (c + 1) for _ in range(c + 1)]
for _ in range(n):
    c1, c2 = map(int, sys.stdin.readline().split())
    graph[c1][c2] = 1
    graph[c2][c1] = 1

q = deque()
visit = [False] * (c + 1)
q.append(1)
visit[1] = True
while q:
    x = q.popleft()
    for i in range(c + 1):
        if graph[x][i] == 1 and not visit[i]:
            q.append(i)
            visit[i] = True
visit[1] = False

answer = 0
for v in visit:
    if v:
        answer += 1
print(answer)
