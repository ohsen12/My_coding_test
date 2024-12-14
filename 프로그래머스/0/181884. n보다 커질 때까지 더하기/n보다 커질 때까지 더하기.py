def solution(numbers, n):
    count = 0
    for i in numbers:
        if count > n:
            break
        else:
            count += i
    return count
        