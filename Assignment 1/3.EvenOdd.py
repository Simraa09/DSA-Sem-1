arr = []
n = int(input("Enter the no of elements: "))
even = 0
odd = 0

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)
    if i%2 == 0:
        even +=1
    else:
        odd += 1
        
print("Array: ",arr)
print("No. of Even nos: ",even)
print("No. of Odd nos: ",odd)

