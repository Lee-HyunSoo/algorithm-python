import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = sys.stdin.readline().split()

    value = deque()
    for i, d in enumerate(data):
        value.append((i, int(d)))
    maxvalue = max(v for k, v in value)

    answer = 0
    while True:
        if value[0][0] == m and value[0][1] == maxvalue:
            print(answer + 1)
            break
        elif value[0][1] != maxvalue:
            value.append(value.popleft())
        elif value[0][1] == maxvalue:
            value.popleft()
            maxvalue = max(v for k, v in value)
            answer += 1
