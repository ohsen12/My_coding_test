# zip 함수는 각 iterable의 요소를 병렬적으로 묶어서 튜플로 반환한다.

def solution(my_strings, parts):
    result = []
    for str, (s, e) in zip(my_strings, parts): #반복문을 돌며 한방에 각각 넣어줌
        result.append(str[s:e+1])
    return ''.join(result)

