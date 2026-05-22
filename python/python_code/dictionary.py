# disctionary ma hm list and tuple ko used kar sakta
#  hai but hm dic ma only values ma 
# list and tuple ko used kar sakta hai key ma nai
# Disct are used to stor data values in key : Valuse pair
# They are unorder, mutable(Changable) & don't allow duplicate keys
#  
# info={
#     "key"  : "value",
#     "Name" : "Niraj",
#     "class" : "MCA-II",
#     "Subject" : ["Python","c","Java"],
#     "SubjCode" :[865,858,565],
#     "Tpoics" : ("Disc","Set"),
#     "Tcode" :  (58,25,65),
#     "Age" : 94,
#     "Mask" : 88.88
#  }
# print(info,type(info))
# print(info["Name"])
# print(info["Tpoics"])
# print(info["Subject"])
# print(info["Age"])
 
# info["Name"] = "Niraj Kr." #it override old valuse
# info["surname"] = "Singh"
# print(info)

# null_dict ={}
# null_dict["Name"] = "Pooja"
# print(null_dict)

#Nested Disctonary
studen = {
    "name" : "Niraj Kumar ",
    "subject" :{
        "phy" : 85,
        "chem" : 95,
        "Maths" :85
    }
}
# print(studen.keys())
# print(list(studen.keys()))
print(list(studen.items()))
