import sys
from collections import Counter

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]

num.sort()
avg = round(sum(num) / len(num))
mid = num[len(num) // 2]
ranges = num[-1] - num[0]

num = Counter(num)
cnt = max(value for value in num.values())
modes = []
for k, v in num.items():
    if v == cnt:
        modes.append(k)
mode = modes[0] if len(modes) == 1 else modes[1]

print(avg)
print(mid)
print(mode)
print(ranges)
