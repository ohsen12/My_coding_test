# range 함수에 세 번째 인자로 -1을 주면 역순의 숫자 시퀀스를 생성할 수 있다.
# 이 경우 첫 번째 인자가 두 번째 인자보다 커야지 음수 스텝 값(-1)과 함께 사용할 수 있다.

def solution(start, end):
    return list(range(start,end-1,-1))