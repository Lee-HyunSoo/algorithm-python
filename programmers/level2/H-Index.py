def solution(citations):
    answer = dict()

    for c1 in citations:
        count = 0
        for c2 in citations:
            if c1 <= c2:
                count += 1

        if c1 < count:
            continue
        else:
            answer[c1] = count
    return max(answer.values()) if answer else 0
