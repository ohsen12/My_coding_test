def solution(arr, intervals):
    l1,l2 = [arr[a:b+1] for a,b in intervals]
    return l1+l2
    
        
    
        