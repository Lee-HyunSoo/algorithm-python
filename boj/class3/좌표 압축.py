import sys

n = int(sys.stdin.readline())
coordinate = list(map(int, sys.stdin.readline().split()))
nums = sorted(coordinate)
nums_dict = dict()

index = 0
for n in nums:
    if n not in nums_dict:
        nums_dict[n] = index
        index += 1

for c in coordinate:
    print(nums_dict[c], end=' ')
