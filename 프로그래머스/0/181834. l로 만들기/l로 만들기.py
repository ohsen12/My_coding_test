# 파이썬에서는 문자열 비교 시 유니코드 코드 포인트를 사용하여 사전순으로 비교한다.
# 유니코드는 각 문자에 고유한 숫자 값을 부여하여 일관된 문자 표현을 가능하게 한다.
# 각 알파벳의 유니코드 코드 포인트는 ord() 함수를 통해 확인할 수 있으며 사전 순으로 커진다.

def solution(myString):
    return ''.join(x if x > 'l' else 'l' for x in myString)