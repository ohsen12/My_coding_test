def solution(arr, queries):
    for i,j in queries:
        arr[i],arr[j] = arr[j],arr[i] #한방에 바꿔줘야 오류 안 남
    return arr