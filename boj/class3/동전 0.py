import sys

n, k = map(int, sys.stdin.readline().split())
value = [int(sys.stdin.readline()) for _ in range(n)]
value.sort(reverse=True)
answer = 0
for v in value:
    if k == 0:
        break
    answer += k // v
    k %= v
print(answer)
