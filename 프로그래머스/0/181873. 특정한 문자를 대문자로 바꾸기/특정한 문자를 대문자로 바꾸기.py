# replace 메서드는 count 옵션 안 주면 문자열 안에 있는 해당 요소를 모두 바꾼다.
def solution(my_string, alp):
    return my_string.replace(alp,alp.upper())