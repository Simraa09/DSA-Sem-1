num = int(input("Enter number: ")) 
rev = 0
n = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if n == rev:
    print("Palindrome")
else:
    print("Not palindrome")