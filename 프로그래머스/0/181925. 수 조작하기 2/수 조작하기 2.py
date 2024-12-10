# 정수배열 첫번째부터 문자열에 따라 조작을 가하고 그 결과값을 numlog 라는 이름의 배열에 기록했다.
# numlog[0]은 아무 조작도 가해지지 않은 첫번째 숫자이다.
# 배열의 마지막 인덱스 = 배열의 길이-1

def solution(numLog):
    dict = {1:'w',-1:'s',10:'d',-10:'a'}
    list = []
    for i in range(len(numLog)):
        if i == len(numLog) -1:  # 마지막 인덱스의 요소는 최종 결과값이니 추가하지 않음
            pass
        else:
            list.append(numLog[i+1]-numLog[i]) # 뒤에서 앞의 요소 빼주면 조작을 가한 값.
    return ''.join(dict[i] for i in list)      # 조작값이랑 대응하는 문자열을 만들어줌
