import sys
from collections import Counter

n = int(sys.stdin.readline())
card = Counter(sys.stdin.readline().split())
m = int(sys.stdin.readline())
data = sys.stdin.readline().split()
for d in data:
    print(card[d])
