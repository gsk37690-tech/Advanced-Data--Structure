def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_of_evens([1, 2, 3, 4, 5, 6]))   
print(sum_of_evens([7, 11, 13, 17]))     
