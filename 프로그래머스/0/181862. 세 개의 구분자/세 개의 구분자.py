# 정규 표현식에서 대괄호 [] 안에 들어가는 문자 클래스는 별도로 따옴표로 감싸지 않아도 된다. 문자 클래스는 그 안에 포함된 문자 중 하나와 일치하는 모든 문자를 나타낸다.r'[abc]'는 a,b,c 로 인식됨
# 문자열의 시작이나 끝 부분에 구분자가 있을 경우와 연속된 구분자가 있을 경우 분할 결과에 빈문자열이 포함될 수 있으므로 리스트 컴프리헨션으로 빈문자열이 아닐 경우에만 배열에 포함시켜주자.

import re 

def solution(str):
    str_list = [i for i in re.split(r'[abc]',str) if i]
    return str_list if str_list else ["EMPTY"]