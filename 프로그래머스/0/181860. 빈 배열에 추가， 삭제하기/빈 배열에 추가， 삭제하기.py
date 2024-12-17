# n개의 원소를 제거하려면 슬라이싱을 [:-n]까지 해주면 됨. 만약 [:-2]라면 끝에서 두 개는 포함하지 않고 자르겠다는 것.

def solution(arr, flag):
    x = []
    for i in range(len(arr)):
        if flag[i]:
            x.extend([arr[i]]*arr[i]*2)
        else:
            x = x[:-arr[i]]
    return x