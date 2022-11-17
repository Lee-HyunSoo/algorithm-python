import sys

while 1:
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    if data[0] == data[1] == data[2] == 0:
        break

    if data[0] ** 2 + data[1] ** 2 == data[2] ** 2:
        print('right')
    else:
        print('wrong')
