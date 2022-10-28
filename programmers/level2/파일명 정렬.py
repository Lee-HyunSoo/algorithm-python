import re


def solution(files):
    sorts = [re.split('([0-9]+)', f) for f in files]
    sorts.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(s) for s in sorts]
