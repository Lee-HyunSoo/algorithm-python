import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().strip()[1:-1].split(','))
    if n == 0:
        arr = deque()

    cnt = 0
    for cmd in p:
        if cmd == 'R':
            cnt += 1
        else:
            if not arr:
                print('error')
                break
            arr.popleft() if cnt % 2 == 0 else arr.pop()
    else:
        if cnt % 2 != 0:
            arr.reverse()
        print('[' + ','.join(arr) + ']')
