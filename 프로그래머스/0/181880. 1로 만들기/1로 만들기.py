def solution(num_list):
    count = 0
    for i in num_list:
        while True:
            if i==1:
                break
            elif i%2:
                i = (i-1)/2
            else:
                i = i/2
            count += 1
    return count