# 서로 다른 k개의 수를 저장한 배열
# 숫자배열 arr에서 수를 하나씩 가져와서, 지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가

def solution(arr, k):
    l = []
    for i in arr:
        if len(l)==k: # 요소의 개수가 k만큼 채워지면 추가를 멈춤
            break
        elif i not in l: # 아직 k만큼 채워지지 않았으면 l의 요소에 없을 경우 추가
            l.append(i)
    if len(l)<k:         # 다 만들어진 배열의 길이가 k보다 작으면 차이만큼 -1로 채워줌
        l.extend([-1]*(k-len(l)))
    return l 