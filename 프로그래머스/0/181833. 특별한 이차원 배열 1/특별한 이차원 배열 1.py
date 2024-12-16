def solution(n):
    # n x n 크기의 이차원 배열 생성 및 초기화
    arr = [[0] * n for _ in range(n)] # _ 은 사용하지 않는 변수. 반복횟수만 중요함.
    
    # i == j인 경우 값을 1로 설정
    for i in range(n): # 배열의 크기 만큼 순회
        arr[i][i] = 1

    return arr