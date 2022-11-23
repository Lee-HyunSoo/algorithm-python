import sys

n, m = map(int, sys.stdin.readline().split())
set_n = set(sys.stdin.readline().strip() for _ in range(n))
set_m = set(sys.stdin.readline().strip() for _ in range(m))
set_nm = list(set_n & set_m)

print(len(set_nm))
for nm in sorted(set_nm):
    print(nm)
