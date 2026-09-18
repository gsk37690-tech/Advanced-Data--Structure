exp = input("Enter Expression to Evaluate:")
print(eval(exp))

n = int(input())
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
print(arr)

s1 = input().split()
intli = []
for x in s1:
    intli.append(eval(x))
print(intli)

#intli = list(eval(x) for x in input().split())

even = [n for n in intlist if n % 2 == 0]
