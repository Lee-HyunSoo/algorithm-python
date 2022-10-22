from collections import deque


def solution(priorities, location):
    answer = 0
    printer = deque((i, value) for i, value in enumerate(priorities))

    while True:
        maxPriority = max([value for i, value in printer])
        if printer[0][0] == location and printer[0][1] == maxPriority:
            return answer + 1
        elif printer[0][1] == maxPriority:
            printer.popleft()
            answer += 1
        else:
            tmp = printer.popleft()
            printer.append(tmp)
