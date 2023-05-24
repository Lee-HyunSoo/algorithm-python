def solution(d, budget):
    answer, sum = 0, 0
    for i in sorted(d):
        sum += i
        if sum > budget:
            return answer
        answer += 1
    return answer
