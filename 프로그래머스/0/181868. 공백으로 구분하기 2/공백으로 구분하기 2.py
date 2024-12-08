#strip 메서드로 문자열 좌우공백 제거하고, split 메서드로 공백을 기준으로 문자열을 나눠담은 리스트를 반환(split()에서 아무것도 지정하지 않으면 기본 구분자가 공백이다)
def solution(my_string):
    return my_string.strip().split()