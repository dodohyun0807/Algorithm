def solution(players, callings):
    answer = []
    chkDict = dict()
    
    for i, v in enumerate(players):
        chkDict[v] = i
        
    for i in callings:
        front = chkDict[i]-1
        overTaker = chkDict[i]
        chkDict[players[front]] = overTaker
        chkDict[players[overTaker]] = front
        players[front],players[overTaker] = players[overTaker],players[front]

    
    return players