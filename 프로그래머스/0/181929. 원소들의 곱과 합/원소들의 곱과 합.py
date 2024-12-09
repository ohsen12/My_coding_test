def solution(num_list):
    n = 1
    for i in num_list:
        n *= i
    return int(n < sum(num_list)**2)