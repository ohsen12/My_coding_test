# not in 연산자는 특정 값이 시퀀스(리스트, 문자열, 튜플 등)에 포함되지 않는지 확인할 때 사용
def solution(my_string):
    return ''.join(i for i in my_string if i not in 'aeiou')