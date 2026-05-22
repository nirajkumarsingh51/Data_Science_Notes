# # collection = {6,1,5,4,"Rays","niraj"}

# # print(collection)
# # print(type(collection))
# # print(len(collection)) #total no of Iteam

# collection = set() # empty set 
# collection.add(5)
# collection.add(2)
# collection.add(2)
# # collection.remove(2)

# collection.add("Sun")
# collection.add((1,5,9)) #tuple Works

# # collection.add([4,5]) #list not wort in set


# print(type(collection))

# # print(collection)

# # collection.clear()
# print(len(collection))
##################################################

# coll = { "Hello","apnacollage","Niraj","pythoncls"}

# print(coll.pop())

####################################################

#Set method 

#1 Set.union(set2)
# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))

#2 set.intersection(set2)
# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.intersection(set2))

# practice section of set 

#Q1.

# disctionary = {
#     "cat" : "a small animal",
#     "table" : ["a pice of furnater", "list of fact & figre"]
# }
# print(disctionary)

#QWAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.2. 

marks ={}

p=int(input("Enter a phys : "))
marks.update({"phys" : p})

p=int(input("Enter a Chem : "))
marks.update({"Chem" : p})

p=int(input("Enter a Maths : "))
marks.update({"Maths" : p})

print(marks)

#Q  Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

