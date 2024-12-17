def transform(arr):
    # 변환 작업 정의
    return [x//2 if x>=50 and x%2==0 else (x*2+1 if x<50 and x%2==1 else x) for x in arr]

def solution(arr):
    count = 0
    while True:
        new_arr = transform(arr)
        if new_arr == arr:
            return count
        arr = new_arr
        count += 1