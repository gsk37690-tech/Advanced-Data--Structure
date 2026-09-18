arr = list(map(int,input().split()))
n = len(arr)
for j in range(n):
    for i in range(n-j-1) :
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i + 1] = temp 

if arr == sorted(arr):
    print("true")
else:
    print("false")
print(arr)
print(arr[-2])

#Let's say arr = [4,5,2]
#i = 0,j = 0:
#arr[0] > arr[1] = 4 > 5, not true no swap
#i = 0,j = 2:
#arr[2] > arr[3] = 5 > 2, true swap
#[4,2,5]
#i = 0,j = 0
#arr[0] > arr[1] = 4 > 2, true swap
#[2,4,5]
