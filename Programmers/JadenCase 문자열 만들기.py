def solution(s):
    temp = s.split(' ')
    arr = []
    
    for word in temp:
        arr.append(word[0].upper() + word[1:].lower())
        
    return ' '.join(arr)