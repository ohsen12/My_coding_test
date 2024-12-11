def solution(s1, s2):
    result = 0
    for a in s1:
        for b in s2:
            if a == b:
                result += 1
    return result