import sys
import math

num = str(math.factorial(int(sys.stdin.readline())))[::-1]
answer = 0
for n in num:
    if n != '0':
        break
    answer += 1
print(answer)
