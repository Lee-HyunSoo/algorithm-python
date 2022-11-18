import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

answer = 0
for l in lst:
    if l == 1:
        continue
    for i in range(2, l):
        if l % i == 0:
            break
    else:
        answer += 1
print(answer)