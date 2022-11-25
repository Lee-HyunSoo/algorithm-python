import sys
from collections import Counter

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    clothes = Counter()
    for _ in range(n):
        cloth, kind = sys.stdin.readline().split()
        clothes[kind] += 1

    answer = 1
    for key in clothes.keys():
        answer *= clothes[key] + 1 # 옷의수 + 안입은 경우의수
    print(answer - 1) # 아무것도 안입은거 빼줌
