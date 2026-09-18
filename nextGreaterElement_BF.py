def next_greater_brute_force(arr):
    n = len(arr)
    result = [-1] * n  # Initialize the result array with -1

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break  # Found the next greater element, break the inner loop

    return result

def monotonic_stack_approach(arr):
    n = len(arr)
    result = [-1] * n  # Initialize the result array with -1
    stack = []  # Stack to keep track of indices

    for i in range(n - 1, -1, -1):  # Traverse the array from right to left
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()  # Pop elements from the stack that are less than or equal to arr[i]

        if stack:
            result[i] = arr[stack[-1]]  # The next greater element is at the index on top of the stack


        stack.append(i)  # Push the current index onto the stack

    return result

def runner():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    print("Input Array:", arr)

    # Brute Force Approach
    brute_force_result = next_greater_brute_force(arr)
    print("Next Greater Elements (Brute Force):", brute_force_result)

    # Monotonic Stack Approach
    monotonic_stack_result = monotonic_stack_approach(arr)
    print("Next Greater Elements (Monotonic Stack):", monotonic_stack_result)

runner()

"""BRUTE FORCE Approach

For every element:

Start searching from the next position.
Keep moving right.
The first element greater than the current element is the answer.
If we reach the end, answer is -1.

MONOTONIC STACK way of approach
"""
"""
Refer Brute Force approach once.

Process the array from right to left and maintain a stack containing useful candidates 
for being the next greater element.

The stack is maintained in decreasing order from bottom to top.

This is called a:
Monotonic Decreasing Stack

DSA Pattern to Remember 

for i in range(n - 1, -1, -1):

    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(arr[i])
"""
