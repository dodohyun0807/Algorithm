def solution(word):
    ans = 0
    wrd = ["A", "E", "I", "O", "U"]
    cnt = [0, 5]

    for i in range(1, 5):
        cnt.append(cnt[i] * 5)

    a = sum(cnt)

    for i in range(1, len(cnt)):
        cnt[i] = a // cnt[i]

    for i in range(len(word)):
        if word[i] == "A":
            ans += 1
        else:
            tmp = cnt[i + 1]
            tmp2 = wrd.index(word[i])
            tmp3 = tmp * tmp2 + 1
            ans += tmp3

    return ans
