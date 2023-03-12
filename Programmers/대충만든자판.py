def solution(keymap, targets):
    answer = []
    
    for target in targets:
        tmp = 0
        for t in target:
            chk = 987654321
            for key in keymap:
                for i in range(len(key)):
                    if key[i] == t and chk > i+1:
                        chk = i+1
            if(chk == 987654321):
                answer.append(-1)
                tmp = 0
                break
            else:
                tmp += chk
        if tmp != 0 :
            answer.append(tmp)
    
    return answer