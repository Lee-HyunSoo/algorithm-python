from collections import Counter
import math

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    jstr1, jstr2 = [], []
    tmp1, tmp2 = '', ''
    for i in range(len(str1)):
        tmp1 += str1[i]
        if len(tmp1) == 2:
            if 'a' <= tmp1[0] <= 'z' and 'a' <= tmp1[1] <= 'z':
                jstr1.append(tmp1)
            tmp1 = tmp1[1:2]

    for i in range(len(str2)):
        tmp2 += str2[i]
        if len(tmp2) == 2:
            if 'a' <= tmp2[0] <= 'z' and 'a' <= tmp2[1] <= 'z':
                jstr2.append(tmp2)
            tmp2 = tmp2[1:2]

    jstr1 = Counter(jstr1)
    jstr2 = Counter(jstr2)

    answer1 = answer2 = 0
    for key, value in jstr1.items():
        if jstr2[key]:
            answer1 += min(value, jstr2[key])
            answer2 += max(value, jstr2[key])
        else:
            answer2 += value
    for key, value in jstr2.items():
        if not jstr1[key]:
            answer2 += value
    return math.trunc(answer1 / answer2 * 65536) if answer2 > 0 else 65536

print(solution("FRANCE", "french"))