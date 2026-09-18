arr = list(map(int,input().split()))
Maximum = max(arr)
Minimum = min(arr)
Sumation = sum(arr)
Avg = Sumation // len(arr)
arr = arr[::-1]
#arr.reverse()

key = int(input())
def binary_search(arr[],key):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = low + (high - low) / 2
        if (arr[mid] == key):
            return mid
        if (arr[mid] < target) :
            low = mid + 1
        else :
            high = mid -1
    return mid
#binary search is part of "DIVIDE AND CONQUER PATTERN" not "TWO POINTER PATTERN" because the pointers are used to define the search window and does not take part in the process.

if (binary_search(arr,key)) print("Key Found at :",binary_search(arr,key))

def countevod(arr):
    odd = 0
    even = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd

#find second largest element
print(b)

