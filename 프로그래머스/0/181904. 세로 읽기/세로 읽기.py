# 사람 기준 c번째 열을 추출하기 위해 c-1로 설정
# c-1번째 인덱스에서부터 m 간격으로 문자를 추출(m글자씩 적었으니까)
# 예를 들어, '101010' 이라는 문자열을 2글자씩 적었고 각각 1번째 열에 적힌 글자를 뽑으라는 상황. 해당 문자열을 0번째 인덱스부터 끝까지 2간격씩 추출한 것과 같다.

def solution(s, m, c):
    return s[c-1::m]
