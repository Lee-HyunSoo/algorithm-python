import sys

k = int(sys.stdin.readline())
stack = []
for _ in range(k):
    num = int(sys.stdin.readline())
    stack.append(num) if num != 0 else stack.pop()
print(sum(stack))
