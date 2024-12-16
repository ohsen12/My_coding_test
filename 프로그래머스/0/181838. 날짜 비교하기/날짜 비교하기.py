def solution(date1, date2):
    # 연도, 월, 일을 차례로 비교
    for d1, d2 in zip(date1, date2):
        if d1 < d2:
            return 1
        elif d1 > d2:
            return 0
    return 0  # 날짜가 동일한 경우 0 반환