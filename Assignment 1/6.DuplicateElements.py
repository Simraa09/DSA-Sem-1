arr = []
n = int(input("Enter the no of elements: "))
unique = []

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    if num not in unique:
        unique.append(num)
    
print("Array: ",arr)
print("Unique Array: ",unique)