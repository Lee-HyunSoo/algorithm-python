import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer, total = 0, 0
for a in sorted(arr):
    total += a
    answer += total
print(answer)
