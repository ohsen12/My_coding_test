# 행의 수 = 배열 원소의 수
# 열의 수 = 배열 원소 그 하나의 길이
# extend 메서드는 **리스트**에 담겨져 있는 요소들을 다른 리스트에 추가할 때 사용한다

def solution(arr):
    r = len(arr)    # 행의 수
    c = len(arr[0]) # 열의 수
    if r>c:
        for i in range(len(arr)):
            arr[i].extend([0]*(r-c))
    elif r<c:
        for i in range(c-r):
            arr.append([0]*c)
    return arr
        
    