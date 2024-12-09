# 요구사항을 차근차근 따라가자
def solution(code):
    mode = 0
    ret = []
    for i,e in enumerate(code):
        if mode == 0:
            if e != '1':          # e는 현재 문자열의 요소라 str이다.
                if i%2 == 0:
                    ret.append(e)
            else:
                mode = 1
        else:
            if e != '1':
                if i%2 == 1:
                    ret.append(e)
            else:
                mode = 0
    return ''.join(ret) if ret else 'EMPTY' # 빈 문자열은 False로 간주된다.
        
    
            