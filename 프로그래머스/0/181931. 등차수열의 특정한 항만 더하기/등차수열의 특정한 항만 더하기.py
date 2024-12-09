# 등차수열 : 연속된 항들 간의 차이가 일정한 수열. 이 일정한 차이를 공차라고 함.

def solution(a, d, included):
    n = 0
    for i, e in enumerate(included):
        if e:
            n+= a+d*i
    return n
            
    