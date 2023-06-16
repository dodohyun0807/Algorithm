from collections import deque


def solution(n, info):
    maxGap = 0
    res = []

    Q = deque()
    Q.append((0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

    while Q:
        target, arr = Q.popleft()

        if sum(arr) == n:
            A, L = 0, 0
            for i in range(11):
                if info[i] != 0 or arr[i] != 0:
                    if info[i] >= arr[i]:
                        A += 10 - i
                    else:
                        L += 10 - i

            if A < L:
                gap = L - A
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arr)

        elif sum(arr) > n:
            continue

        elif target == 10:
            tmp = arr.copy()
            tmp[target] = n - sum(tmp)
            Q.append((-1, tmp))

        else:
            tmp = arr.copy()
            tmp[target] = info[target] + 1
            Q.append((target + 1, tmp))
            tmp2 = arr.copy()
            tmp2[target] = 0
            Q.append((target + 1, tmp2))

    if not res:
        return [-1]

    elif len(res) == 1:
        return res[0]

    else:
        return res[-1]
