#
# p=[20]
# p=[5,'Rays',5,8,7]
# print(p,type(p))

p=[5,'rays',20,5,7]
# print(p[0:5])
# print(p[0:3])
# print(p[1:])
# print(p[1:3])
# print(p[1][2])
# print(p[1][-2])
# print(p[-4][-2])
# print(p[-4][2])

###########################################################################
#Method of List

# p=[]
# p=[20]
p=[5,2,15,10,4.5,10]
print(p,type(p))
# p[1]=20
# p[1:3]=[12,19]
# p[1:3]=[12,19,23]
# q=p.append(120)
# q=p.insert(1,30)
# q=p.insert(1,[1,3,9])
# q=p.extend([1,3,9])
# q=p.extend((1,3,9))
# q=p.clear()
# q=p.remove(110)
# q=p.pop()
# q=p.pop(1)
# q=p.count(10)
# q=p.index(30)
# q=p.reverse()
# q=p.sort()
q=p.sort(reverse=True)
print(p)
print(q)