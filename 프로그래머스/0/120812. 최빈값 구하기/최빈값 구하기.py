from collections import Counter

def solution(array):
    # 배열의 각 값의 빈도를 계산합니다.
    counter = Counter(array)
    
    # 빈도 리스트를 생성합니다. (값, 빈도) 형태의 튜플로 이루어진 리스트
    freq_list = counter.most_common()
    
    # 가장 높은 빈도와 해당 빈도를 가지는 값들의 리스트를 추출합니다.
    max_freq = freq_list[0][1]
    most_common_values = [item[0] for item in freq_list if item[1] == max_freq]
    
    # 최빈값이 여러 개인지 확인하고 결과를 반환합니다.
    if len(most_common_values) > 1:
        return -1
    else:
        return most_common_values[0]