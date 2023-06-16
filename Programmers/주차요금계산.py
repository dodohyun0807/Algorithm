import math


def solution(fees, records):
    count = {}
    result = {}

    for i in records:
        tmp = i.split()
        if tmp[2] == "IN":
            count[tmp[1]] = int(tmp[0][:2]) * 60 + int(tmp[0][3:])
        else:
            outT = int(tmp[0][:2]) * 60 + int(tmp[0][3:])
            total = outT - count[tmp[1]]
            del count[tmp[1]]
            if tmp[1] in result:
                result[tmp[1]] = total + result[tmp[1]]
            else:
                result[tmp[1]] = total

    if count:
        for i in count:
            if i in result:
                temp = result[i]
                result[i] = (1439 - count[i]) + temp
            else:
                result[i] = 1439 - count[i]

    for i in result:
        if result[i] <= fees[0]:
            result[i] = fees[1]
        else:
            temp = math.ceil((result[i] - fees[0]) / fees[2])
            f = (temp * fees[3]) + fees[1]
            result[i] = f

    return [i[1] for i in sorted(result.items())]
