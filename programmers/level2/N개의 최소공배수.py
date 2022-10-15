def solution(arr):
    answer = min(arr)
    while True:
        for n in arr:
            if answer % n != 0:
                break
        else:
            return answer
        answer += min(arr)
