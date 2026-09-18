def two_sum(num,target):
    left = 0
    right = len(num) - 1
    while left < right:
        current_sum = num[left] + num[right]
        print("left : ", left, "Right : ", right, "Current Sum : ", current_sum, "Target : ",target)
        if current_sum == target:
            return[left,right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return[-1,-1]

arr = list(map(int,input("Enter List:").split()))
arr = sorted(arr)
key = int(input("Enter Target:"))
print(arr)
print(two_sum(arr,key))
