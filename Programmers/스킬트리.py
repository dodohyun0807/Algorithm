def solution(skill, skill_trees):
    answer = 0
    
    for user in skill_trees:
        idx = -1
        cnt = 0
        for i in user:
            if i in skill:
                if idx+1 != skill.find(i):
                    break
                else:
                    idx = skill.find(i)
                    cnt += 1
            else:
                cnt += 1
                continue
        
        if cnt == len(user):
            answer += 1

    return answer