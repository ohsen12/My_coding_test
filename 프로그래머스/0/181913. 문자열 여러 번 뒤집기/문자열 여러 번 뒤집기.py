# str은 reverse 메서드 못 씀. 이건 리스트에만 사용가능 (reversed() 함수는 여러 시퀀스형 가능)
# 슬라이싱 [시작:끝:간격]에서 끝 숫자는 포함되지 않는다.
# str을 아예 뒤집는 방법은 역순 슬라이싱이다. [ : : -1]
# 인덱스 s-1까지 + 뒤집은 부분(s부터 e까지) + e+1부터 마지막까지

def solution(my_string, queries):
    for s,e in queries:
        str1 = my_string[s:e+1]    # 인덱스 s부터 e까지
        str2 = ''.join(reversed(str1))
        my_string = my_string[:s] + str2 + my_string[e+1:] # 문자열 다시 만들어주기
    return my_string