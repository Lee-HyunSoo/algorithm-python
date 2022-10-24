import math
from collections import defaultdict


def solution(fees, records):
    records = [record.split(' ') for record in records]
    answer, stack = [], []
    cars = defaultdict(int)

    for record in sorted(records, key=lambda x: x[1]):
        if record[2] == 'IN':
            stack.append(record)
        else:
            tmp1, tmp2 = stack[-1][0].split(':'), record[0].split(':')
            hour1, hour2, min1, min2 = int(tmp1[0]), int(tmp2[0]), int(tmp1[1]), int(tmp2[1])
            total_minute = 0
            if tmp1[1] > tmp2[1]:
                total_minute += ((hour2 - hour1 - 1) * 60) + min2 + (60 - min1)
            else:
                total_minute += ((hour2 - hour1) * 60) + (min2 - min1)
            cars[record[1]] += total_minute
            stack.pop()

    for s in stack:
        tmp = s[0].split(':')
        hour, minute = int(tmp[0]), int(tmp[1])
        cars[s[1]] += ((23 - hour) * 60) + (59 - minute)

    for key, value in sorted(cars.items()):
        if value > fees[0]:
            answer.append(fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer
