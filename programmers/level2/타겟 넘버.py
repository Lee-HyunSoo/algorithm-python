from collections import deque


def solution(numbers, target):
    # return dfs(numbers, target, 0, 0)
    return bfs(numbers, target)


def dfs(numbers, target, idx, value):
    if idx == len(numbers):
        return 1 if value == target else 0
    result = 0
    result += dfs(numbers, target, idx + 1, value + numbers[idx])
    result += dfs(numbers, target, idx + 1, value - numbers[idx])
    return result


def bfs(numbers, target):
    answer = 0
    q = deque([(0, -numbers[0]), (0, numbers[0])])

    while q:
        idx, value = q.popleft()

        if idx == len(numbers) - 1:
            answer += 1 if value == target else 0
        else:
            for data in [(idx + 1, value - numbers[idx + 1]), (idx + 1, value + numbers[idx + 1])]:
                q.append(data)
    return answer
