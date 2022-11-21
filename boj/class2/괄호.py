import sys

n = int(sys.stdin.readline())
for _ in range(n):
    data = sys.stdin.readline().strip()
    stack = []
    for d in data:
        if d == '(':
            stack.append(d)
        elif d == ')':
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')