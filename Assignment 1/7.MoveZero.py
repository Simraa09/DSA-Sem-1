arr = []
n = int(input("Enter the no of elements: "))
count = 0

for i in range(n):
    num = int(input("Enter the number: "))
    if num == 0:
        count += 1
        continue
    arr.append(num)
for i in range(count):
    arr.append(0)
    
print("Array: ",arr)
