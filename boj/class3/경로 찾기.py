import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
