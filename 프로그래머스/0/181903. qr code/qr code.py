# code의 각 인덱스 : 0,1,2,3,4... 

def solution(q, r, code):
    list = []
    for i, e in enumerate(code):
        if i%q == r:
            list.append(e)
    return ''.join(list)