from BST import BST

def product_pair_check_bst(arr,target):
    tree = BST()
    for data in arr:
        tree.add(data)
    for data in arr:
        if target % data == 0:
            required = target // data
            if tree.search(tree.root, required):
                if required != data or arr.count(data) >= 2:
                    print(f"Pair found: {data} and {required}")
                    return True
                else:
                    return False
    return False

def product_pair_check(arr, target):
    found = False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] == target:
                print(f"Pair found: {arr[i]} and {arr[j]}")
                found = True
                break
    if not found:
        print("No pair found")

    return found


arr = [1,3,5,7,9]
target = 15

















































































































































































3