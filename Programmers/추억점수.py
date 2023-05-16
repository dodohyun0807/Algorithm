def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        temp = 0
        for i in people:
            if i in name:
                idx = name.index(i)
                temp += yearning[idx]
        
        answer.append(temp)
        
    
    return answer