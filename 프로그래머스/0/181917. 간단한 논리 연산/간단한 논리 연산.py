# ∧ 는 and(둘 다 참이어야 참), ∨는 or(하나만 참이어도 참)
# (x1 | x2) & (x3 | x4) 로도 가능하다.

def solution(x1, x2, x3, x4):
    return (x1 or x2)and(x3 or x4)
    