# sorted() 함수는 원본데이터는 변경하지 않고, 정렬된 새로운 리스트를 반환한다.

def solution(array):
    return sorted(array)[len(array) // 2]