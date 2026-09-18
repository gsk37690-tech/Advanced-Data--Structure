def intersection(a,b):
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result

a = list(map(int,input("Enter List A :").split()))
b = list(map(int,input("Enter List B :").split()))

print ("Intersection:",intersection(a,b))

#Finding Similar ELements within two lists.
#then making another list to append these elements inside that list.
#make an intersection. 


