def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        tmp = ''
        for s in skills:
            if s in skill:
                tmp += s
        if skill[:len(tmp)] == tmp:
            answer += 1
    return answer
