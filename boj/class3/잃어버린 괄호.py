import sys

data = sys.stdin.readline().strip().split('-')
nums = []
for d in data:
    nums.append(list(map(int, d.split('+'))))
answer = sum(nums[0])
for i in range(1, len(nums)):
    answer -= sum(nums[i])
print(answer)
