def max_consecutive_ones(nums):
    count = 0
    maxi = 0
    for num in nums:
        if num == 1:
            count += 1
            maxi = max(maxi,count)
        else:
            count = 0
    return maxi
arr = [1,1,0,1,0]
print(max_consecutive_ones(arr))
