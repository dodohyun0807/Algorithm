def solution(record):
    user = {}
    answer = []
    
    for i in range(len(record)):
        a = record[i].split()
        if a[0] != 'Leave':
            user[a[1]] = a[2]
    
    for j in range(len(record)):
        nu = record[j].split()
        u = nu[1]

        if nu[0] == 'Change':
            pass
        else:
            if nu[0] == 'Enter':
                answer.append('{}님이 들어왔습니다.'.format(user[u]))
            else:
                answer.append('{}님이 나갔습니다.'.format(user[u]))

    
    return answer