import sys

n = int(sys.stdin.readline())
start, answer = 1, 1
for i in range(1, n):
    answer += 1
    start += 6 * i
    if n <= start:
        break
print(answer)
