def solution(arr):
    if 2 not in arr:
        return [-1]
    start = arr.index(2)      # 2가 처음으로 나오는 인덱스
    end = len(arr) - arr[::-1].index(2)  # 2가 마지막으로 나오는 인덱스 계산
    return arr[start:end] 