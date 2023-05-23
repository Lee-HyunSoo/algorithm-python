import re


def solution(phone_number):
    return re.sub("[0-9]", "*", phone_number, len(phone_number) - 4) if len(phone_number) > 4 else phone_number
