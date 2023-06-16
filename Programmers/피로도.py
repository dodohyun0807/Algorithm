def solution(k, dungeons):
    answer = 0
    visited = [0] * len(dungeons)

    def check(k, cnt):
        nonlocal answer

        if cnt > answer:
            answer = cnt

        for idx in range(len(dungeons)):
            if dungeons[idx][0] <= k and visited[idx] == 0:
                visited[idx] = 1
                check(k - dungeons[idx][1], cnt + 1)
                visited[idx] = 0

    check(k, 0)

    return answer
