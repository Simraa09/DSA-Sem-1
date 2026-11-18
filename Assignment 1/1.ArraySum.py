arr = []
sum = 0
n = int(input("Enter the no of elements: "))

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    sum += num

print("Array: ",arr)
print("Sum of elements: ",sum)