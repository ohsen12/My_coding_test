def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)] # p는 세 번 나온 숫자
        q = nums[counts.index(1)] # q는 한 번 나온 숫자
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2: # 두 쌍의 값이 같은 경우
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else: # 한 쌍의 값이 같고 나머지 두 값이 다를 때
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)
