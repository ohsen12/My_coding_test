# 약수의 쌍을 알면 된다. (a,b)에서 a를 기준으로 곱했을 때 n이 되는 b를 찾자.
# 𝑛을 나누어 떨어지게 하는 숫자 𝑎와𝑏가 존재할 때, 이들 𝑎와𝑏는 약수 쌍을 이룬다.

def solution(n):
    count = 0
    for a in range(1, n + 1): # n 이하의 숫자
        if n % a == 0:  # n이 a로 나누어떨어지는지 확인 (a가 n의 약수인지 확인)
            b = n // a  # a와 곱해서 n이 되는 b 값을 계산
            count += 1  # 순서쌍 (a, b) 발견 시 카운트 증가
    return count