n = int(input("Enter number: ")) 
sum = 0
for i in range (1,n+1):
    sum += i**3
print(sum)

# OR

s = ((n * (n+1)) // 2) **2
print (s)