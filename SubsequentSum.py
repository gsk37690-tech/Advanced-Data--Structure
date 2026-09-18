def subsequentsum(arr,index,current,current_sum,target):

    if index == len(arr):
        if current_sum == target:
            print(current)
        return
    
    current.append(arr[index])
    subsequentsum(arr,index+1,current,current_sum+arr[index],target)

    current.pop()
    subsequentsum(arr,index+1,current,current_sum,target)

def runner():
    arr = list(map(int,input("Enter List:").split()))
    target = int(input("Enter Target:"))
    subsequentsum(arr,0,[],0,target)

runner()
