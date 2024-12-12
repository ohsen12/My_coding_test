# 자연수 : 보통 0을 제외한 양의 정수(int)
# math 모듈의 sprt() 함수는 숫자를 입력받아 그 수의 제곱근을 구해준다.

import math

def solution(n):
    sqrt_n = int(math.sqrt(n)) # 제곱수는 양의 정수를 곱해서 나오는 수이므로 소수점 이하 떼준다
    if sqrt_n * sqrt_n == n:
        return 1  # n이 제곱수인 경우
    else:
        return 2  # n이 제곱수가 아닌 경우