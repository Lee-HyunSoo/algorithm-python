def solution(record):
    ids, access, answer = dict(), [], []

    for r in record:
        command = r.split(' ')
        if command[0] == 'Enter':
            access.append((command[0], command[1]))
            ids[command[1]] = command[2]
        elif command[0] == 'Leave':
            access.append((command[0], command[1]))
        else:
            ids[command[1]] = command[2]

    for a in access:
        if a[0] == 'Enter':
            answer.append(ids[a[1]] + "님이 들어왔습니다.")
        else:
            answer.append(ids[a[1]] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))