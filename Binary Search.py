arr = list(map(int,input().split()))
key = int(input())
def binary_search(arr,key):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = low + (high - low) // 2
        if (arr[mid] == key):
            return mid
        if (arr[mid] < key) :
            low = mid + 1
        else :
            high = mid -1
    return mid
#binary search is part of "DIVIDE AND CONQUER PATTERN" not "TWO POINTER PATTERN" because the pointers are used to define the search window and does not take part in the process.

def lower_bound(arr,target):
    high = len(arr) - 1
    low = 0
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upper_bound(arr,target):
    high = len(arr) - 1
    low = 0
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid - 1
            high = mid - 1
        else:
            low = mid + 1
    return ans

if (binary_search(arr,key)):
    print("Key Found at :",binary_search(arr,key))
if (lower_bound(arr,key)):
    print("Key Found at :",lower_bound(arr,key))
if (upper_bound(arr,key)):
    print("Key Found at :",upper_bound(arr,key))
            
