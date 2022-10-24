from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[False] * m for _ in range(n)]
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = deque([(0, 0, 1)])
    visit[0][0] = True
    while q:
        y, x, answer = q.popleft()

        if y == n - 1 and x == m - 1:
            return answer

        for dy, dx in dxy:
            if 0 <= y + dy < n and 0 <= x + dx < m:
                if maps[y + dy][x + dx] == 1 and not visit[y + dy][x + dx]:
                    q.append((y + dy, x + dx, answer + 1))
                    visit[y + dy][x + dx] = True
    return -1
