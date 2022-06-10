def solution(clothes):
    answer = 0
    arr = {}
    
    for i in clothes:
        if not i[1] in arr:
            arr[i[1]] = [i[0]]
            arr[i[1]].append(0)
        else:
            arr[i[1]].append(i[0])
            
    for i in arr:
        if answer == 0:
            answer += len(arr[i])
        else:
            answer *= len(arr[i])
    
    return answer-1