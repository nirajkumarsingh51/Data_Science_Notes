#Accept two no from keyboard , check and disply lcf except 1.
a=int(input("Enter first No.    : "))
b=int(input("Enter a Second No. : "))
if a<b:
    n=a
else:
    n=b
for d in range(2,n+1):
    if a%d==0 and b%d==0:
        h=d
        break
print("Lowest  commmon factor: ",h)