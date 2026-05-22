import pandas as pd

tbl_students = {
    "Name": ["Aman", "Niraj", "Rahul"],
    "Marks": [90, 85, 78]   
}
df = pd.DataFrame(tbl_students)
print(df)



import pandas as pd
tbl_bihar = {
    "City" : ["Patna", "Gaya", "Bhagalpur"],
    "Population" : [2.5, 1.5, 1.0]
}

df =pd.DataFrame(tbl_bihar)

print(df,type(df))

print(df.head(1))


