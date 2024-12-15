def solution(arr, idx):
    for i in range(idx,len(arr)):
        if arr[i] in [1]:
            return i
    return -1 #반복문을 다 돌았는데 1이 없었다면 -1을 반환
        
    
        
        