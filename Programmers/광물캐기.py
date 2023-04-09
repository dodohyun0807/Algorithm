def solution(picks, minerals):
    ans = 0
    
    totalGok = sum(picks) * 5
    
    if totalGok < len(minerals):
        minerals = minerals[:totalGok]
    
    lenM = len(minerals)
    info = []
    temp = [0,0,0]
    idx = 1
    
    for i in range(lenM):
        if minerals[i] == 'diamond':
            temp[0] += 1
            temp[1] += 5
            temp[2] += 25
        
        if minerals[i] == 'iron':
            temp[0] += 1
            temp[1] += 1
            temp[2] += 5
            
        if minerals[i] == 'stone':
            temp[0] += 1
            temp[1] += 1
            temp[2] += 1
        
        if i+1 == 5 * idx or i+1 == lenM:
            idx += 1
            info.append(temp)
            temp = [0,0,0]
    
    info.sort(key = lambda x : (x[2], x[1], x[0]))
    
    idx = 0
    
    while info:
        t = info.pop()
        if picks[idx] > 0:
            ans += t[idx]
            picks[idx] -= 1
        
        else:
            idx += 1
            info.append(t)
    
    
    return ans