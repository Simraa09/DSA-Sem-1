num = int(input("Enter number: ")) 
sum = 0
org = num
len = len(str(num))
while num > 0:
    sum += (num % 10)** len
    num //= 10
if org == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")