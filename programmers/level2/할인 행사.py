from collections import Counter


def solution(want, number, discount):
    answer = 0
    sale = dict({want[i]: number[i] for i in range(len(want))})

    for i in range(len(discount)):
        if i + 10 <= len(discount):
            for key, values in Counter(discount[i: i + 10]).items():
                if key not in sale or sale[key] != values:
                    break
            else:
                answer += 1
    return answer
