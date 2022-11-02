def solution(a, b):
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day = 0
    for i in range(0, a):
        day += months[i]
    day += b
    return week[day % 7 - 1]
