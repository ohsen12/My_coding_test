def solution(intStrs, k, s, l):
    list = []
    for i in intStrs:
        int_i = int(i[s:s+l])
        if int_i > k:
            list.append(int(i[s:s+l]))
    return list