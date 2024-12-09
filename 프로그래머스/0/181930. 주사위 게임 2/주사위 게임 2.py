def solution(a, b, c):
    n1 = a+b+c
    n2 = a**2+b**2+c**2
    n3 = a**3+b**3+c**3
    if a == b == c:
        return n1*n2*n3
    elif a != b and b != c and a != c:
        return n1
    else:
        return n1*n2
            