import sys

a, b, v = map(int, sys.stdin.readline().split())
v -= a
answer = v // (a - b) if v % (a - b) == 0 else (v // (a - b)) + 1
print(answer + 1)
