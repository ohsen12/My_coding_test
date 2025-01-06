def solution(a):
    a.sort()
    # 음수 중 절대값이 가장 큰 두 수의 곱 vs 양수 중 가장 큰 두 수의 곱
    return max(a[0]*a[1],a[-1]*a[-2])