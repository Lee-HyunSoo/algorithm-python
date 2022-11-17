import sys

n = int(sys.stdin.readline())
answer = []
for i in range(666, sys.maxsize):
    if len(answer) > n:
        break
    if '666' in str(i):
        answer.append(i)
print(answer[n - 1])
