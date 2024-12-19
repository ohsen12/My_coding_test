def solution(strarr):
    l = [len(i) for i in strarr] # 각 요소의 길이 세주기(배열요소 최대길이 구하기 위함)
    tu_list = [(i,0) for i in range(1,max(l)+1)] # 길이:등장횟수 딕셔너리를 위한 튜플딕
    my_dict = dict(tu_list) 
    for i in strarr:
        my_dict[len(i)] +=1 # 해당 길이 키의 값에 +=1 해주기
    return max(my_dict.values()) # 가장 큰 값 구하기
        
        