# map 함수는 함수를 각각의 요소에 적용한 이터레이터를 반환하고 sum 함수는 이터레이터를 인자로 받아 그 합계를 구해준다.

def solution(num_str):
    return sum(map(int,num_str))