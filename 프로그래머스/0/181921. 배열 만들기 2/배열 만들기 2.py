# 정수는 단일값이라서 인덱스가 없다. 하나의 정수의 길이는 그 자체로 1임.
# all() 함수는 반복가능한객체의 모든 요소가 참(True)인지 확인한다. 모든 요소가 참이면 True를 반환하고, 하나라도 거짓(False)이면 False를 반환한다.
# 조건식이 반복문 범위내에서 모두 참인지 확인

def solution(l, r):
    list = []
    for i in range(l,r+1):
        str_i = str(i)     #스트링화 해야지 얘를 for문이랑 인덱스 돌릴 수 있음
        if all(char in ['0','5'] for char in str_i):
            list.append(i)
    return list if list else [-1]