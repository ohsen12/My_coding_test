# 장군j 5 , 병정b 3, 일i 1

def solution(hp):
    # 24
    j1,j2 = divmod(hp,5)  # j1:4,j2:4
    b1,b2 = divmod(j2,3)  # b1:1,b2:1
    i1,i2 = divmod(b2,1)  # i1:1,i2:0
    return j1+b1+i1