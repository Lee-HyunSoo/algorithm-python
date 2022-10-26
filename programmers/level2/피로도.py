from itertools import permutations


def solution(k, dungeons):
    answer = []
    dungeons = list(permutations(dungeons, len(dungeons)))
    for dungeon in dungeons:
        tired, score = k, 0
        for d in dungeon:
            if tired >= d[0]:
                tired -= d[1]
                score += 1
        answer.append(score)
    return max(answer)


print(solution(80, [[80,20],[50,40],[30,10]]))


