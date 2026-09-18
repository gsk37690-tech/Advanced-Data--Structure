def solve(arr,index,current):

    if index == len(arr):
        print(current)
        return
    
    current.append(arr[index])
    solve(arr,index+1,current)

    current.pop()
    solve(arr,index+1,current)

def runner():
    arr = list(map(int,input("Enter List:").split()))
    solve(arr,0,[])
runner()