def solution(numbers):
    strnum = list(map(str, numbers))
    strnum.sort(key=lambda x: x * 3)
    return str(int(''.join(reversed(strnum))))
