# not(b)는 b가 False인 경우 True가 되므로, 해당 인덱스 a의 문자가 리스트에 포함된다.

def solution(str, bool):
    return [str[a] for a,b in enumerate(bool) if not(b)]
    