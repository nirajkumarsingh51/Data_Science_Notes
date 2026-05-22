# wap to acept a no from keyboard to check and display a massage wether give no is  prime, composite 
# or neither prime nor compositve
n=int(input("Enter a no : "))
d=2
while d<=n/2:
    if n%d==0:
        d=n
    d=d+1
if n==1:

    print("Neither prime, Nor Composite.")
elif d>n:
    print("Composite.")
else:
    print("Prime! ")