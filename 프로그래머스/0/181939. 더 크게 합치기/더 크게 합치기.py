def solution(a,b):    
    a = str(a)
    b = str(b)
    n1 = int(a+b)
    n2 = int(b+a)
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return n1
