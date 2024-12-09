# join 함수는 문자열 리스트에 사용할 수 있다.

def solution(num_list):
    l1 = []
    l2 = []
    for i in num_list:
        if i % 2 == 1:
            l1.append(str(i))
        elif i % 2 == 0:
            l2.append(str(i))
    return int(''.join(l1)) + int(''.join(l2))