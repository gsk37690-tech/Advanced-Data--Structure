from collections import deque

def shortest_subarray(arr, k):

    prefix = [0]

    for num in arr:
        prefix.append(prefix[-1] + num)

    dq = deque()
    ans = len(arr) + 1

    for j in range(len(prefix)):

        while dq and prefix[j] - prefix[dq[0]] >= k:
            ans = min(ans, j - dq.popleft())

        while dq and prefix[j] <= prefix[dq[-1]]:
            dq.pop()

        dq.append(j)
    if ans == len(arr) + 1:
        return -1
    
    return ans,dq,prefix

def runner():
    arr = list(map(int, input("Enter List:").split()))
    k = int(input("Enter Target:"))
    print(arr)
    print(shortest_subarray(arr, k))

runner()

# why dequeue have indexes so that program can utilize both index and values.
# The indexes allow the program to keep track of the positions of the elements in the original array, which is necessary for calculating the length of the subarray.
# Why are we removing elements in dequeue, because they are not in increasing order which will destabilize the dequeue.