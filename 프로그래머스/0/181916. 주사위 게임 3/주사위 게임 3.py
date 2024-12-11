# 중복 개념이 나오면 항상 set을 떠올리자.

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {x: dice.count(x) for x in dice}
    
    # 모든 주사위 숫자가 같을 때
    if len(counts) == 1:
        return 1111 * a
    
    # 세 주사위가 같을 때
    elif 3 in counts.values():
        p = [k for k, v in counts.items() if v == 3][0]
        q = [k for k, v in counts.items() if v == 1][0]
        return (10 * p + q) ** 2
    
    # 두 쌍의 주사위 값이 같을 때
    elif list(counts.values()).count(2) == 2:
        p, q = sorted(counts.keys())
        return (p + q) * abs(p - q)
    
    # 두 주사위가 같고 나머지 두 개의 값이 다를 때
    elif 2 in counts.values():
        p = [k for k, v in counts.items() if v == 2][0]
        q, r = [k for k, v in counts.items() if v == 1]
        return q * r
    
    # 모두 다른 숫자인 경우
    else:
        return min(dice)