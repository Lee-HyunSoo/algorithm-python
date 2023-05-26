def solution(k, score):
    answer, glory = [], []
    for s in score:
        if len(glory) < k:
            glory.append(s)
        else:
            if s > min(glory):
                glory.remove(min(glory))
                glory.append(s)
        answer.append(min(glory))
    return answer
