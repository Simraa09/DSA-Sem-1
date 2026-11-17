n = 5
for i in range(n):
    print(" " * (n-i+1), end="")
    for j in range (2*i+1):
        print(chr(65+j),end=" ")
        
    print()
print()

n = 5
for i in range(n):
    print(" " * (n-i), end="")
    for j in range (i+1):
        print(chr(65+i),end=" ")
    print()
print()

n = 5
num = 0
for i in range(n):
    print(" " * (n-i), end="")
    for j in range (i+1):
        print(chr(65+num),end=" ")
        num += 1
    print()
print()