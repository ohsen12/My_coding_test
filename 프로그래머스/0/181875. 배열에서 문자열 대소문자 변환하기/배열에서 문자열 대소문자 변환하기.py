def solution(strArr):
    for i in range(len(strArr)):
        if i %2 == 1:
            strArr[i] = strArr[i].upper() # 리스트 값 바꿔주기
        elif i %2 == 0:
            strArr[i] = strArr[i].lower()
    return strArr
            