# 지금 n*n 배열이 아님에 유의! j의 범주는 board 안의 하나의 요소를 순회할 수 있도록 해줘야 함.

def solution(board, k):
    n = len(board)
    total = 0
    for i in range(n):
        for j in range(len(board[i])):
            if i + j <= k:
                total += board[i][j]
    return total