def solution(order):
    answer = 0
    stack = []
    num = 1
    
    for i in order:
        chk = False
        while True:
            if len(stack) == 0:
                stack.append(num)
                num+=1
            if i > stack[-1]:
                stack.append(num)
                num+=1
            elif i == stack[-1]:
                answer += 1
                stack.pop()
                chk = True
                break
            else:
                break
        if chk == False:
            break
    
    return answer