dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    answer = 9999999999
    global total
    total = 999999999

    cx = characterX * 2
    cy = characterY * 2
    ix = itemX * 2
    iy = itemY * 2

    D = [[0] * 103 for _ in range(103)]
    V = [[0] * 103 for _ in range(103)]
    V[cx][cy] = 1

    for i in rectangle:
        for j in range(i[0] * 2, (i[2] * 2) + 1):
            for k in range(i[1] * 2, (i[3] * 2) + 1):
                D[j][k] = 1

    for i in rectangle:
        for j in range((i[0] * 2) + 1, i[2] * 2):
            for k in range((i[1] * 2) + 1, i[3] * 2):
                D[j][k] = 0

    def dfs(x, y, cnt):
        global answer
        global total

        if x == ix and y == iy:
            if answer > cnt:
                answer = cnt

        for i in range(4):
            dc = x + dx[i]
            dr = y + dy[i]
            if cnt > 2 and dc == cx and dr == cy:
                if total > cnt + 1:
                    total = cnt + 1

            if D[dc][dr] == 1 and V[dc][dr] == 0:
                V[dc][dr] = 1
                dfs(dc, dr, cnt + 1)

    dfs(cx, cy, 0)

    answer2 = total - answer

    if answer > answer2:
        return answer2 // 2
    else:
        return answer // 2
