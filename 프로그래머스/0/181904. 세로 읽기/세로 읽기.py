def solution(my_string, m, c):
    temp=[]
    temp2= list(my_string)
    idx=0 

    for i in temp2: 
        idx += 1
        if m == c :
            if idx % m == 0 : # 마지막 열을 읽는 경우.
                temp += i 

        elif idx % m == c : # 1~ m-1열 중 하나를 읽는 경우.
            temp += i 



    temp = ''.join(map(str,temp))  
    answer = temp

    return answer