import sys

l = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

answer = 0
for index, w in enumerate(word):
    num = ord(w) - 96
    tmp = 1
    for i in range(index):
        tmp *= 31
        tmp %= 1234567891
    answer += num * tmp
print(answer % 1234567891)
