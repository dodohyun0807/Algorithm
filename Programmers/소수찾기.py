from itertools import *

def solution(numbers):
    answer = 0
    
    # 경우의 수
    
    num_division = []
    
    for i in numbers:
        num_division.append(i)
    
    num_make = []
    
    for i in range(1, len(numbers)+1):
        num_make += list(permutations(num_division, i))

    
    arr = []
    
    for i in num_make:
        check = int(('').join(i))
        if check != 0 and not check in arr:
            arr.append(check)
    
    # 소수 판별
    
    for n in arr:
        if n < 2:
            continue
        
        isPN = True
        
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                isPN = False
                break
        
        if isPN:
            answer += 1

    return answer