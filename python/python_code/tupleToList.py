p=('apple','orange','mango')
print(p,type(p))
# p[1]='Banana'
p=list(p) #convert tuple to list
p[1]="Banana"
p.append("Papaya")
print(p,type(p))
p=tuple(p) #convert list to tuple
# p[2]="rays"
print(p,type(p))
