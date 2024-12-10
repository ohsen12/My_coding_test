def solution(n):
    pizza, remain = divmod(n, 7)
    if remain != 0: #사람 수가 피자 한판 수보다 많다면 
        pizza += 1  #피자 수에 +1 해주기
    return pizza
        