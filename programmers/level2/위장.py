from collections import defaultdict


def solution(clothes):
    answer = 1
    clothesDic = defaultdict(int)
    for cloth in clothes:
        clothesDic[cloth[1]] += 1

    for key, value in clothesDic.items():
        answer *= (value + 1) # + 1을 통해 옷 가지수 + 안입는 경우
    return answer - 1 # -1을 통해 아무것도 안입는 경우의수 뺌
