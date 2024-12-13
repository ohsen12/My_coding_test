# strip으로 받은 문자열 앞 뒤로 공백 없애주고, split으로 공백을 구분으로 요소를 나눠서 리스트로 반환.

str1, str2 = input().strip().split(' ')
print(str1+str2)