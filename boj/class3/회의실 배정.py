import sys

n = int(sys.stdin.readline())
meets = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meets.append((start, end))
meets.sort(key=lambda x: (x[1], x[0]))

answer = 1
end = meets[0][1]
for i in range(1, len(meets)):
    if meets[i][0] >= end:
        end = meets[i][1]
        answer += 1
print(answer)
