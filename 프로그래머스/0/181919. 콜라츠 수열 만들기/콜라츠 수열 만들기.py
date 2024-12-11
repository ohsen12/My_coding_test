def solution(n):
    list = [n]
    while True:
        if list[-1] == 1:
            break
        elif n%2 == 0:
            n /= 2
            list.append(n)
        else:
            n = 3*n +1
            list.append(n)
    return list
    