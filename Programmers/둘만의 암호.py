def solution(s, skip, index):
    answer = ''
    alp = []
    
    for i in range(97, 123):
        tmp = chr(i)
        alp.append(tmp)
    
    for i in s:
        idx = alp.index(i)
        cnt = 0
        
        while True:
            if idx == len(alp):
                idx = 0
                continue
            
            if alp[idx] in skip:
                idx += 1
                continue
            
            if cnt == int(index):
                answer += alp[idx]
                break
            
            cnt += 1
            idx += 1
                
    return answer