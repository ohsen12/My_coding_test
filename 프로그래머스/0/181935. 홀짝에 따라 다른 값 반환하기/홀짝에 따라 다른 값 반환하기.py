def solution(n):
    if n %2 == 1:
        num = 0
        for i in range(n+1):
            if i %2 == 1:
                num += i
        return num
    else:
        num = 0
        for i in range(n+1):
            if i %2 == 0:
                num += i**2
        return num
                