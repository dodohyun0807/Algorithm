def solution(commands):
    ans = []
    maps = [list(0 for _ in range(51)) for _ in range(51)]
    it = [list((j, i) for i in range(51)) for j in range(51)]
    idx = 0

    while idx != len(commands):
        o = commands[idx].split(" ")
        if o[0] == "UPDATE":
            if len(o) == 3:
                for i in range(51):
                    for j in range(51):
                        if maps[i][j] == o[1]:
                            maps[i][j] = o[2]
            else:
                y1, x1 = it[int(o[1])][int(o[2])]
                for i in range(51):
                    for j in range(51):
                        if it[i][j] == (y1, x1):
                            maps[i][j] = o[3]

        if o[0] == "MERGE":
            y1, x1 = it[int(o[1])][int(o[2])]
            y2, x2 = it[int(o[3])][int(o[4])]
            if maps[y1][x1] == 0:
                maps[y1][x1] = maps[y2][x2]
            for i in range(51):
                for j in range(51):
                    if it[i][j] == (y2, x2):
                        it[i][j] = (y1, x1)

        if o[0] == "UNMERGE":
            y1, x1 = it[int(o[1])][int(o[2])]
            temp = maps[y1][x1]
            for i in range(51):
                for j in range(51):
                    if it[i][j] == (y1, x1):
                        it[i][j] = (i, j)
                        maps[i][j] = 0
            maps[int(o[1])][int(o[2])] = temp

        if o[0] == "PRINT":
            y1, x1 = it[int(o[1])][int(o[2])]
            if maps[y1][x1] == 0:
                ans.append("EMPTY")
            else:
                ans.append(maps[y1][x1])

        idx += 1

    return ans
