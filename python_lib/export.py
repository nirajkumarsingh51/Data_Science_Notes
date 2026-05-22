import pandas as pd

data={
    'Name': ['Niraj', 'Suman', 'Rohit', 'Sita', 'Gita'],
    'Marks': [80, 90, 75, 85, 95],
    'Age': [20, 21, 22, 23, 24]
}

df = pd.DataFrame(data)
df.to_csv("student.xlsx")
# print(df)