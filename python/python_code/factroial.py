#wap in python language to acept a number and disply its factorial
# n=int(input("Enter a no. : "))
# fact =1
# while n>0:
#     fact=fact*n
#     n=n-1
# print("The factorial is : ",fact)

# using for loop:
n=int(input("Enter a no. : "))
fact =1
for n in range(n,0,-1):
    fact=fact*n
print("The factorial is : ",fact)