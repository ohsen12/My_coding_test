import string

# 소문자 알파벳 리스트 생성. string 모듈에 포함된 상수(소문자알파벳문자열)
lower_str = string.ascii_lowercase

# 대문자 알파벳 리스트 생성. string 모듈에 포함된 상수(대문자알파벳문자열)
upper_str = string.ascii_uppercase

def solution(my_string):
    upper_count = []
    lower_count = []
    for i in upper_str:
        upper_count.append(my_string.count(i))
    for i in lower_str:
        lower_count.append(my_string.count(i))
    return upper_count + lower_count