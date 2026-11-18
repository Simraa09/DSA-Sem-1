# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 3:
#             for k in range (1,i+1):
#                 print("*",end="")
#                 break
#         elif i == 3:
#             for k in range (1,n+1):
#                 print("*",end="")
#                 break
#         else:
#             print(" ",end="")
#     print()

        
n = 7

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 4 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()