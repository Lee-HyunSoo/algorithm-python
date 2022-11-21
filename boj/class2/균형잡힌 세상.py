import sys

while 1:
    data = sys.stdin.readline()
    if data == '.\n':
        break
    stack, flag = [], False
    for d in data:
        if d == '(':
            stack.append(d)
        elif d == '[':
            stack.append(d)
        elif d == ')':
            if not stack or stack[-1] == '[':
                flag = True
                break
            stack.pop()
        elif d == ']':
            if not stack or stack[-1] == '(':
                flag = True
                break
            stack.pop()
    if not stack and not flag:
        print('yes')
    else:
        print('no')
