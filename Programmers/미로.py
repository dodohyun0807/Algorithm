def solution(maps):
    mapLen = len(maps[0])
    startIdx = [0, 0]
    labIdx = [0, 0]
    visited = []
    xx = [1, 0, -1, 0]
    yy = [0, -1, 0, 1]
    cntL, cntE = 0, 0

    # start지점 찾고 방문 배열에 방문으로 처리하기
    for i in range(len(maps)):
        visitArr = []
        for j in range(mapLen):
            visitArr.append(0)
            if maps[i][j] == "S":
                startIdx[0], startIdx[1] = i, j
                visitArr.pop()
                visitArr.append(1)
            if maps[i][j] == "L":
                labIdx[0], labIdx[1] = i, j
        visited.append(visitArr)

    # 시작인덱스 기준으로 dfs시작
    def dfs(x, y, cnt, t, labCnt, extCnt):
        for i in range(4):
            dx = x + xx[i]
            dy = y + yy[i]
            if t == "L":
                if (
                    0 <= dx < mapLen
                    and 0 <= dy < len(maps)
                    and maps[dy][dx] != "X"
                    and visited[dy][dx] == 0
                ):
                    print(maps[dy][dx])
                    if maps[dy][dx] == "L":
                        if cnt + 1 < labCnt:
                            labCnt = cnt + 1
                            cntL = labCnt
                        print(cntL)
                        continue
                    visited[dy][dx] = 1
                    dfs(dx, dy, cnt + 1, t, labCnt, extCnt)

            elif t == "E":
                if (
                    0 <= dx < mapLen
                    and 0 <= dy < len(maps)
                    and maps[dy][dx] != "X"
                    and visited[dy][dx] == 0
                ):
                    if maps[dy][dx] == "E":
                        if cnt + 1 < extCnt:
                            extCnt = cnt + 1
                        return extCnt
                    visited[dy][dx] = 1
                    dfs(dx, dy, cnt + 1, t, labCnt, extCnt)

    dfs(startIdx[0], startIdx[1], 0, "L", 987654321, 987654321)

    for i in range(len(visited)):
        for j in range(mapLen):
            visited[i][j] = 0

    dfs(labIdx[0], labIdx[1], 0, "E", 987654321, 987654321)

    return


# ============================================================================================================================================================

arr = [
    ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"],
    ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"],
    ["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"],
]

for i in arr:
    solution(i)
    print("=============================")
