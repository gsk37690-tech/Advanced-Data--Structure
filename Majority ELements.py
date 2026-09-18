def majority_elements(arr):
    candidate = 0
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
arr = list(map(int,input().split()))
print("The most Common Element is:",majority_elements(arr))

#the candidate is the counting element and the count checks the no of the occuring element.
