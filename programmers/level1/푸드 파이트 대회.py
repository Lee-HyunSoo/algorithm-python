def solution(food):
    answer = ''
    for i, f in enumerate(food):
        if i != 0:
            answer += str(i) * int(f / 2)
    return answer + '0' + ''.join(reversed(list(answer)))
