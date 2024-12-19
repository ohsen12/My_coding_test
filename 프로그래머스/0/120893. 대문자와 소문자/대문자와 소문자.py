# 조건식이 if로만 존재할 때: [표현식 for i in 리스트 if 조건식]
# 조건식에 if와 else가 모두 있을 때 : [표현식 if 조건식 else 다른 표현식 for i in 리스트]

def solution(my):
    return ''.join(i.lower() if i.isupper() else i.upper() for i in list(my))