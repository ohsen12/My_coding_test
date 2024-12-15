# 슬라이싱이란 건.. 참 유용한 듯

def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2])) 