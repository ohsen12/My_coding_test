def solution(array):
    num = 0
    data = 0
    for i in set(array):
        if array.count(i) > num:
            num = array.count(i)
            data = i
        elif array.count(i) == num: # i의 빈도가 현재 최빈값의 빈도 num과 같다면, 최빈값이 여러 개인 경우
            data = -1
    return data