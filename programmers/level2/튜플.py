import re


def solution(s):
    answer = []
    s = s.split("{")
    s.sort(key=lambda x:len(x))

    for num in s:
        num = re.findall('\d+', num)
        for i in num:
            if answer.count(int(i)) == 0:
                answer.append(int(i))
    return answer
