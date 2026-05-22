# #p=()
# #p=(20) 
# #p=(20,)
# p=(5,'rays',5,20)
# # print(p[0:5]),
# # print(p[:3])
# # print(p[0:3])
# # print(p[1:])
# # print(p[1:3])

# # print(p[1][2])
# print(p[1][1])
# print(p[1][-3])
# print(p[-3][1])
# print(p[-3][-3])


# p=()
# p=(20)
# p=('rays')
# p=(20,)
# p=('rays',)
p=(5,'rays',10,4.5,10)
print(p,type(p))
# p[1]=20
# q=p.count(10)
q=p.index(10)
print(p)
print(q)
