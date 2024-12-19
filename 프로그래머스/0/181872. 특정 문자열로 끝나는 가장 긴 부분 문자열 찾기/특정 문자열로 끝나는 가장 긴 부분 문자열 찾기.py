def solution(str, pat):
    for i in range(len(str)):
        if str.startswith(pat,i): #해당 인덱스부터의 str이 pat으로 시작한다면,
            if str[i:].count(pat)>1: #만약 하위 문자열에 pat이 더 남아있다면
                continue # 다음 인덱스로 넘어가서 검토
            else:
                str = str[:i+len(pat)] #pat을 포함한 지점까지 슬라이싱 하기
    return str

'''
# 다른 풀이 
def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

# AAabc 와 ab의 경우, cbaAA에서 (전체 길이 5 - ba가 처음으로 나타나는 인덱스 1) = 4를 끝값으로 두고 자르면 pat이 끝나는 지점까지 자를 수 있다.
'''