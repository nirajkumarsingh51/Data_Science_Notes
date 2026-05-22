p=[12,5,23,4]
# q=p #not duplicate copy
# q=p.copy() #making duplicate
q=list(p) #making duplicate
p.append(25)
print(p)
print(q)
if p is q:
    print("Not duplicate")
else:
    print("duplicate")