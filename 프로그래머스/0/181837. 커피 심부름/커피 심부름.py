# 아메리카노 4500 라떼 5000

def solution(order):
    pat1,pat2 = 'americano','cafelatte'
    a,c = 0,0
    for i in order:
        if i=='anything':
            a+=1
        elif pat1 in i:
            a+=1
        elif pat2 in i:
            c+=1
    return 4500*a + 5000*c
    