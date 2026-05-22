#wap to accept a no from keyboard calculate and display the reverse.
n=int(input("Enter a no. : "))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("Reverse is :",rev)
