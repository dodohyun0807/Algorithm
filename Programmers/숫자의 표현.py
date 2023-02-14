def solution(n):
    answer = 1
    
    for i in range(1, (n//2)+1):
        cnt = i
        for j in range(i+1, (n//2)+2):
            cnt += j
            if cnt == n:
                answer += 1
            if cnt > n:
                break
    
    return answer