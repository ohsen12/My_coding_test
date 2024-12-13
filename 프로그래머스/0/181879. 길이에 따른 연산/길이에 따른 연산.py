# ''로 감싸진 식을 그대로 실행할 수 있는 eval() 함수. 실무에선 지양하라고 한다.

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return eval('*'.join(map(str, num_list)))