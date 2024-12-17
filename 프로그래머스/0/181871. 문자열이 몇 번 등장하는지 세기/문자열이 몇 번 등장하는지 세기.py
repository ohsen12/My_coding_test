# 문자열의 find 메서드는 문자열에서 특정 서브스트링이 처음으로 등장하는 위치를 찾는 데 사용한다. 이 메서드는 서브스트링의 시작 인덱스를 반환하며, 서브스트링이 없으면 -1을 반환한다.

def solution(myString, pat):
    count = 0
    start = 0
    while start < len(myString): # 탐색 시작 위치 start가 문자열의 길이를 초과하지 않도록
        i = myString.find(pat, start) # pat이 시작하는 인덱스(start) 찾기
        if i != -1: # 없어서 -1을 반환한게 아니라면 있다는 거니까
            count += 1 # 카운트해주고
            start = i + 1  # 중복된 패턴을 찾기 위해 시작 위치를 바로 그 다음으로 1씩 이동
        else: # -1을 반환한다면
            break
    return count