def solution(age):
    key = [str(i) for i in range(10)]
    value = [chr(i) for i in range(97, 108)]
    d = dict(zip(key, value))
    return ''.join(d[i] for i in str(age))