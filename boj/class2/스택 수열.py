import sys

n = int(sys.stdin.readline())
seq = [int(sys.stdin.readline()) for _ in range(n)]
num, stack, answer = 1, [], []

while len(seq) > 0:
    if stack and stack[-1] == seq[0]:
        stack.pop()
        seq.pop(0)
        answer.append('-')
    elif num > n:
        print('NO')
        break
    else:
        stack.append(num)
        num += 1
        answer.append('+')
else:
    for a in answer:
        print(a)
