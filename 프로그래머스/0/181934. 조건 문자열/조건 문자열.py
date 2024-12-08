# eval 함수는 문자열로 표현된 코드를 실행할 수 있는 함수

def solution(ineq, eq, n, m):
    if eq == '!':
        condition = f'{n}{ineq}{m}'
    else:
        condition = f'{n}{ineq}{eq}{m}'
    return 1 if eval(condition) else 0

