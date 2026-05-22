p={12,7,'rays',20}
# q=p
# q=p.copy()
q=set(p)
p.add(24)
print(p)
print(q)
if p is q:
    print("Not duplicate")
else:
    print("Duplicate")