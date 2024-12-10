def solution(arr, queries):
    l1 = []
    for s,e,k in queries:
        l2 = []
        for i in range(s,e+1):
            if arr[i] > k:
                l2.append(arr[i]) #k보다 큰 값 추가 
        if l2:                    #k보다 큰 값 추가한 게 빈문자열(False)이 아니라면
            l1.append(min(l2))    #l2의 최소값 추가해주기(k보다 크면서 가장 작은 값)
        else:
            l1.append(-1)         #빈 문자열이면 -1 추가해주기
    return l1