from collections import deque

def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n+1)]
    d = [-1] * (n+1)
    
    for i in edge:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
        
    q = deque([1])
    d[1] = 0
    
    while q:
        current = q.popleft()
        
        for i in arr[current]:
            if d[i] == -1:
                q.append(i)
                d[i] = d[current] + 1
                
    for i in d:
        if i == max(d):
            answer += 1
    
    
    return answer