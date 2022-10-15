from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    answer = 0

    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.pop()
        answer += 1
    return answer if not people else answer + len(people)
