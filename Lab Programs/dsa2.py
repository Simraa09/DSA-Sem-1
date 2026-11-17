arr = [11,2,3,11,4,5,10]
max = arr[0]
min = arr[0]
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i
print("Max number is : ", max)
print("Min number is : ", min)