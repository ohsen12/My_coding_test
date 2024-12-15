def solution(str1):
    while '0' in str1: # 0이 str1에 존재한다면 아래의 조건을 고려해야 함
        if str1.index('0') == 0: # 0이 처음에 오면 없애주는 반복을 돌림
            str1 = str1.replace('0', '', 1)
        else: # 0이 처음에 안오면 반복문을 빠져나감
            break
    return str1 # 반복문을 거쳐 처린된 str1 or 0이 아예 str1에 없었던 경우
