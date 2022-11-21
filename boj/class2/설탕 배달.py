import sys

n = int(sys.stdin.readline())
sugar = [float('inf')] * (n + 1)
sugar[3] = 1
if n >= 5:
    sugar[5] = 1

for i in range(6, n + 1):
    sugar[i] = min(sugar[i - 3] + 1, sugar[i - 5] + 1)
print(sugar[n] if sugar[n] != float('inf') else -1)






