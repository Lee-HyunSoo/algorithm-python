import sys

k, n = map(int, sys.stdin.readline().split())
rope = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(rope)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for r in rope:
        cnt += r // mid

    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)
