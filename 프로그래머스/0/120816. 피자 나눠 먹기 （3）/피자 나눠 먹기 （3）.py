def solution(slice, n):
    pizza, remain = divmod(n,slice)
    if remain != 0:
        return pizza +1
    else:
        return pizza