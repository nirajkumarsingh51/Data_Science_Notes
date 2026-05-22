#wap to accept n no from keyboard , to check gretes and least number
n=int(input("How Many No. You Want : "))
i=1
while i<=n:
    num=int(input("Enter a no :"))
    if i==1:
        gt=lt=num
    elif num>gt:
        gt=num
    elif num<lt:
        lt=num
    i=i+1
print("Gretest no: ",gt,"\nleast no: ",lt)
