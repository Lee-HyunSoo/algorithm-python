import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y, 0])

for i in range(len(lst)):
    cnt = 0
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
            cnt += 1
    lst[i][2] = cnt + 1

for l in lst:
    print(l[2], end=' ')
