#wap to accept 10 number from keyboard to count and  display even or odd no
i=1
even=odd=0
while i<=10:
    num=int(input("Enter a no :"))
    if num%2==0:
        even=even+1
    else:
        odd=odd+1        
    i=i+1
print("Total even no =",even, "\n Total odd =",odd)
