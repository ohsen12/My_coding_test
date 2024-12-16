def solution(my):
    str = 'abcdefghijk'
    my = list(my)
    for i in range(len(my)):
        if my[i] in str:
            my[i] = 'l'
    return ''.join(my)
            