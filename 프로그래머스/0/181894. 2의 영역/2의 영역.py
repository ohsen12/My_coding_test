def solution(arr):
    try:
        start = arr.index(2)  # 첫 번째 2의 인덱스 찾기
        end = len(arr) - 1 - arr[::-1].index(2)  # 마지막 2의 인덱스 찾기
        return arr[start:end + 1]
    except: #2가 없으면 에러가 발생하므로 [-1] 반환
        return [-1]