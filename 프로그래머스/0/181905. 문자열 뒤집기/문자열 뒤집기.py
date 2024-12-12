def solution(my, s, e):
    mid = ''.join(reversed(my[s:e+1]))
    return my[:s] + mid + my[e+1:]