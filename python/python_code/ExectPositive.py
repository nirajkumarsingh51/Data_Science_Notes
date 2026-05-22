# accept exectly 5 possitve number from keyboard and display ts same on monitor:
i=1
p=[]
while i<=5:
    n=int(input("Enter a Values of "+str(i)+" Positon :"))
    if n<=0:
        continue
    p.append(n)
    i=i+1
print("Exect Five Positve Numbers are : ",p)

