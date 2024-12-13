def solution(my_string):
    list = []
    for i in my_string: #문자열의 모든 요소에 대해
        try:
            if int(i)%1 == 0: #자연수를 1로 나누면 나머지가 0
                list.append(int(i))
        except ValueError:
            continue
    return sum(list)
            