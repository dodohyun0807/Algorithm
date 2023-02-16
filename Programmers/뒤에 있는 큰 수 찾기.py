def solution(numbers):
    answer = [-1] * len(numbers)
    
    stack = []
    
    for i in range(len(numbers)):
        temp = numbers[i]
        while stack and numbers[stack[-1]] < temp :
            answer[stack.pop()] = temp
        
        stack.append(i)

    return answer