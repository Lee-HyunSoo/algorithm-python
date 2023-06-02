def solution(n, m, section):
    answer = 0

    wall = [1] * (n + 1)
    for s in section:
        wall[s] = 0

    while 0 in wall:
        for i in range(1, len(wall)):
            if wall[i] == 0:
                for j in range(i, i + m):
                    if j < len(wall):
                        wall[j] = 1
                    else:
                        break
                answer += 1
    return answer
