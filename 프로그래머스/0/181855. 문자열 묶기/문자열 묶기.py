def solution(strarr):
    l = [len(i) for i in strarr] # 각 요소의 길이 세주기(배열요소 최대길이 구하기 위함)
    tu_list = [(i,0) for i in range(1,max(l)+1)] # 길이:등장횟수 딕셔너리를 위한 튜플딕
    my_dict = dict(tu_list) 
    for i in strarr:
        my_dict[len(i)] +=1 # 해당 길이 키의 값에 +=1 해주기
    return max(my_dict.values()) # 가장 큰 값 구하기

'''
# 메모리 사용이 덜 한 풀이
def solution(strArr):
    m = {}
    for s in strArr:
        if len(s) in m:     # 해당 길이의 키가 이미 있다면
            m[len(s)] += 1  # 그 키의 값을 +=1 해주기
        else:
            m[len(s)] = 1   # 새로운 길이가 있을 때마다 해당길이 키를 생성해주기
    return max(m.values())
'''
        
        