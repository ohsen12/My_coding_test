# 두 이터러블의 길이가 다를 때 zip 함수는 짧은 이터러블의 길이에 맞춰 작동한다. 즉, 짧은 이터러블의 끝에서 반복을 멈춘다.
# n개의 원소를 제거하려면 슬라이싱을 [:-n]까지 해주면 됨. 만약 [:-2]라면 끝에서 두 개는 포함하지 않고 자르겠다는 것.


def solution(arr, flag):
    x = []
    for i,j in zip(arr,flag):
        if j:
            x.extend([i]*i*2)
        else:
            x = x[:-i]
    return x