arr = []
n = int(input("Enter the no of elements: "))

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)

arr = sorted(set(arr))

print("Array: ",arr)
print("Smallest:", arr[0])
print("Second Smallest:", arr[1])
print("Largest:", arr[-1])
print("Second Largest:", arr[-2])