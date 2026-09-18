def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = cur
    return arr
arr = list(map(int,input().split()))
print(insertion_sort(arr))

#Takes a Value every loop and checks if before value is greater and then swaps them.
#at last the current value is stored at the end.



