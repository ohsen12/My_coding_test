def solution(arr):
    n = len(arr)
    for i in range(n): # 배열의 크기만큼 범주를 정해준다.
        for j in range(n):
            if arr[i][j] != arr[j][i]: # 전체 배열 검토
                return 0
    return 1