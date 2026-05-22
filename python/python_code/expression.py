# a=int(input("Enter a first no :"))
# b=int(input("Enter a second no :"))
# print("a = ",a,"b = ",b)

# r=a/b

# print("Result is : ", r)

a=int(input("Enter a first no :"))
b=int(input("Enter a second no :"))
print("a = ",a,"b = ",b)
try:
    r=a/b
    print("Result is : ", r)
except:
    print("second value must be not zero ")
