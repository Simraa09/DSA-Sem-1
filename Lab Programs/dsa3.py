arr = [11,2,3,11,4,5,10]
max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

second_max = arr[0]
second_min = arr[0]     
for i in arr:
    if i != max:
        if i > second_max:
            second_max = i
        if i < second_min:
            second_min = i
print("Max number is : ", max)
print("Min number is : ", min)
print("2nd Max number is : ", second_max)
print("2nd Min number is : ", second_min)