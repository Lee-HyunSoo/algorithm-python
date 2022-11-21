import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push_front':
        q.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        q.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(q.popleft() if q else -1)
    elif cmd[0] == 'pop_back':
        print(q.pop() if q else -1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(0 if q else 1)
    elif cmd[0] == 'front':
        print(q[0] if q else -1)
    elif cmd[0] == 'back':
        print(q[-1] if q else -1)
