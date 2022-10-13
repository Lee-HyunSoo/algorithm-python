def solution(s):
    binaryCnt, zeroCnt = 0, 0
    while s != "1":
        zeroCnt += s.count('0')
        s = s.replace('0', '')
        binaryCnt += 1
        s = str(format(len(s), 'b'))
    return [binaryCnt, zeroCnt]
