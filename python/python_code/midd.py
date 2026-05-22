#Wap to accept three no from keyboard , and check the middel values.
#kjdkdfadkl 

a=int(input("Enter 1 no. : "))
b=int(input("Enter a 2 no. : "))
c=int(input("Enter a 3rd No. "))

if a>b:
    if b>c:
         print("B is Middel",b)
    elif a>c:
         print("C is Middel",c)
    else:
         print("A is Middel",a)

else:
    if a>c:
        print("A is Middel",a)
    elif b>c:
        print("C is Middel",c)
    else:
        print("B is Middel",b)
