# 동일한 글자 수의 접두사(앞에서부터 몇 글자)는 하나 밖에 없다는 점을 이용

def solution(my_string, str):
    if my_string[:len(str)] == str:
        return 1
    else:
        return 0