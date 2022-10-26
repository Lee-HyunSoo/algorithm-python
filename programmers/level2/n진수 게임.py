def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)  # 몫, 나머지
    return convert(q, base) + T[r] if q else T[r]


def solution(n, t, m, p):
    answer, numbers, num = '', '', 0
    while True:
        numbers += convert(num, n)
        num += 1
        if len(answer) == t:
            break

        if len(numbers) > p:
            answer += numbers[p - 1]
            p += m

    return answer
