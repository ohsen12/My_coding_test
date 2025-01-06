def solution(n):
    p = 6
    
    # 피자 조각 수가 사람 수로 나눠떨어질 때까지 피자 판 수를 늘려야 함
    while p % n != 0:
        p += 6
    
    # 총 피자 판 수 반환하기
    return p//6 
        