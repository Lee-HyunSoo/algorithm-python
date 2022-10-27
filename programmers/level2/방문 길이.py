def solution(dirs):
    answer = set()
    x, y = 0, 0

    for d in dirs:
        if d == 'U' and y < 5:
            answer.add(((x, y), (x, y + 1)))
            y += 1
        elif d == 'D' and y > -5:
            answer.add(((x, y - 1), (x, y)))
            y -= 1
        elif d == 'L' and x > -5:
            answer.add(((x - 1, y), (x, y)))
            x -= 1
        elif d == 'R' and x < 5:
            answer.add(((x, y), (x + 1, y)))
            x += 1
    return len(answer)
