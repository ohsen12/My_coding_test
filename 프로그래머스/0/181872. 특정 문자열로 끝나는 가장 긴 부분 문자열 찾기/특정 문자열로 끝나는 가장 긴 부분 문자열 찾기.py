def solution(str, pat):
    for i in range(len(str)):
        if str.startswith(pat,i): #해당 인덱스부터의 str이 pat으로 시작한다면,
            if str[i:].count(pat)>1: #만약 하위 문자열에 pat이 더 남아있다면
                continue # 다음 인덱스로 넘어가서 검토
            else:
                str = str[:i+len(pat)] #pat을 포함한 지점까지 슬라이싱 하기
    return str
    