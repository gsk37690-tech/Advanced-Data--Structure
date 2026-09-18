#selection sort takes a min_index value each loop,
#checks the rest of the values in list for a smaller value,
#swaps with that value.
#and then leaves the sorted index alone.
#moves on to the second index keeping the min_index as the next value,
#right after the swapped min value


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

arr = list(map(int,input().split()))
selection_sort(arr)
print(arr)

#["9",2,7,6,5]
#[2,"9",7,6,5]
#[2,5,"7",6,9]
#[2,5,6,"7",9]
#[2,5,6,7,9]


                
