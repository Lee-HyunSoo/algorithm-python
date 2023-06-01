def solution(N, stages):
    defeats = {}
    for i in range(1, N + 1):
        fail, player = 0, 0
        for s in stages:
            if s >= i:
                player += 1
            if s == i:
                fail += 1
        defeats.setdefault(i, 0) if player == 0 else defeats.setdefault(i, fail / player)

    answer = sorted(defeats.items(), key=lambda x: x[1], reverse=True)
    return [key for key, value in answer]
