def solution(arr):
    n = 1
    while n < len(arr): # arr의 길이랑 가장 가까운 2의 거듭제곱 찾기
        n *= 2
    arr += [0] * (n - len(arr)) # n이랑 arr 길이의 차이 구해서 그만큼 0 추가하기
    return arr
