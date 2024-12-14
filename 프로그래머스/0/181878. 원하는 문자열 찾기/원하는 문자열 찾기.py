def solution(str, pat):
    str = str.lower()
    pat = pat.lower()
    return 1 if pat in str else 0