def solution(my, pat):
    my = my.replace('A','b').replace('B','a')
    my = my.upper()
    return int(pat in my)