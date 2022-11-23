import sys

n, m = map(int, sys.stdin.readline().split())
site = dict()
for _ in range(n):
    address, pw = sys.stdin.readline().split()
    site[address] = pw
for _ in range(m):
    print(site[sys.stdin.readline().strip()])
