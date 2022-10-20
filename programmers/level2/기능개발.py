from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses, speeds = deque(progresses), deque(speeds)

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()

        if cnt != 0:
            answer.append(cnt)
    return answer


