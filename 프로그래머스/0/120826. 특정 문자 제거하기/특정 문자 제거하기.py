# [리스트 컴프리헨션 식] 에서 [] 없이 바로 사용할 수 있다.

solution = lambda my_string,letter : ''.join(i for i in my_string if i != letter)