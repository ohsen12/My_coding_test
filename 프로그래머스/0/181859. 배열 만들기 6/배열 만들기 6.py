# 논리 연산자 or는 조건식으로 사용할 때와 표현식으로 사용할 때 약간 다르게 동작한다.
# 조건식으로 사용될 때 or 연산자는 첫번째가 참이면 두번째는 평가하지 않고 True를 반환한다.
# or 연산자가 표현식으로 사용될 때는 첫번째 값이 참인 경우 첫번째를 반환하고 두번째 값은 아예 평가되지 않는다.

def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    return stk or [-1]   #stk가 빈배열이 아니라면 True라서 stk 반환되고 후건은 평가되지 않고 끝난다.