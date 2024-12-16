def solution(my, pat):
    my = my.replace('A','b').replace('B','a').upper()
    return int(pat in my)