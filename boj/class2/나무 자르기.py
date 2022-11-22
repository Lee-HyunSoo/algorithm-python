import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2

    answer = 0
    for t in tree:
        if t >= mid:
            answer += t - mid
    if answer < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)

