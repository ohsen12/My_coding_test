def solution(list):
    l1 = []
    l2 = []
    for i in range(len(list)):
        if i%2==0:
            l1.append(list[i])
        else:
            l2.append(list[i])
    return max(sum(l1),sum(l2))