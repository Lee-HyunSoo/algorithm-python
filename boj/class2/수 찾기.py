import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
num = dict()
for a in arr:
    num[a] = 0

m = int(sys.stdin.readline())
brr = sys.stdin.readline().split()
for b in brr:
    print(1 if num.get(b) == 0 else 0)
