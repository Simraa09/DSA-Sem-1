arr = []
n = int(input("Enter the no of elements: "))

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
search = int(input("Enter number to search: "))

for i in range (len(arr)):
    if arr[i] == search:
        print("Number found!")
        print("Position of number: ",i)
        break
else:
    print("Number not present in arr")
        
