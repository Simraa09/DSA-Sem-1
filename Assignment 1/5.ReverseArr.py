arr = []
n = int(input("Enter the no of elements: "))

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    
print("Array: ",arr)
print("Reversed Array: ",arr[::-1])