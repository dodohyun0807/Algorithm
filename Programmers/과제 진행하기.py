from collections import deque

def solution(plans):
    answer = []
    plans.sort(key = lambda x : (x[1]))    
    pp = []

    for i in plans:
        pp.append([i[0], int(i[1][:2]) * 60 + int(i[1][3:]), int(i[2])])
        
    t = pp[0][1]
    p = deque(pp)
    q = deque()
    l = deque()
    q.appendleft(p.popleft())

    while True:
        if not p and not q and not l:
            break

        if q:
            q[0][2] -= 1
            if q[0][2] == 0:
                answer.append(q.popleft()[0])
                
        if not q and l:
            l[0][2] -= 1
            if l[0][2] == 0:
                answer.append(l.popleft()[0])
    
        if p and t == p[0][1]:
            q.appendleft(p.popleft())
            l.appendleft(q.pop())
    
        t += 1
    
    return answer