def solution(s):
    answer = []
    dic = dict()
    for i, c in enumerate(s):
        if c not in dic.keys():
            answer.append(-1)
        else:
            answer.append(i - dic[c])
        dic[c] = i
    return answer
