import sys

n = int(sys.stdin.readline())
for _ in range(n):
    h, w, n = map(int, sys.stdin.readline().split())
    answer = []
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            answer.append(str(j) + '0' + str(i) if i < 10 else str(j) + str(i))
    print(answer[n - 1])
