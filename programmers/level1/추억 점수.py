def solution(name, yearning, photo):
    answer = []
    dic = {n: y for n, y in zip(name, yearning)}

    for names in photo:
        sum = 0
        for n in names:
            if n not in dic.keys():
                continue
            sum += dic[n]
        answer.append(sum)
    return answer
