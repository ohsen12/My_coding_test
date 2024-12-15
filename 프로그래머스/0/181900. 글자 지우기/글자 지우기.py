# replace 는 카운트 옵션을 줘도 해당 패턴이 첫 번째로 나타나는 부분을 바꾸기 때문에 적절x

def solution(str, indices):
    str = list(str)
    for i in indices: #리스트로 바꾸고 아예 그 인덱스 값을 공백으로 수정
        str[i] = ''
    return ''.join(str) #붙여서 리턴하기