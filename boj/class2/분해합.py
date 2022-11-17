import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
    answer = i
    for j in str(i):
        answer += int(j)
    if answer == n:
        print(i)
        break
else:
    print(0)
