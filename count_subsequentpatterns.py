def count_subsequences(arr,index,current,current_sum,target,count):

    if index == len(arr):
        if current_sum == target:
            return 1
        return 0
    current.append(arr[index])
    take = count_subsequences(arr,index+1,current,current_sum+arr[index],target,count)

    current.pop()
    not_take = count_subsequences(arr,index+1,current,current_sum,target,count)

    return take + not_take

def runner():
    arr = list(map(int,input("Enter List:").split()))
    target = int(input("Enter Target:"))
    count = count_subsequences(arr,0,[],0,target,0)
    print(count)

runner()