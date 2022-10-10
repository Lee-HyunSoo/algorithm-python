def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for c in new_id:
        if not c.isnumeric() and not c.isalpha() and c != '.' and c != '-' and c != '_':
            new_id = new_id.replace(c, '')
    # 3단계
    while new_id.find('..') != -1:
        new_id = new_id.replace('..', '.')
    # 4단계
    new_id = new_id.strip('.')
    # 5단계
    if not new_id:
        new_id += 'a'
    # 6단계
    while len(new_id) >= 16:
        new_id = new_id[:-1]
    new_id = new_id.rstrip('.')
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id

print(solution("abcdefghijklmn.p"))
