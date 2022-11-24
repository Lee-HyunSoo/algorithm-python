import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

answer = start
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for t in tree:
        if t >= mid:
            tmp += t - mid

    if tmp < m:
        end = mid - 1
    else:
        start = mid + 1
        answer = max(answer, mid)
print(answer)
