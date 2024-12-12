def solution(my_string, str):
    l = [my_string[i:] for i in range(len(my_string))]
    return 1 if str in l else 0