# 2d-array

import pandas as pd

student = pd.DataFrame({
    'Name': ['Niraj', 'Suman', 'Rohit', 'Sita', 'Gita'],
    'Marks': [80, 90, 75, 85, 95],
    'Age': [20, 21, 22, 23, 24]
})

df = pd.DataFrame(student)
# df['Grade'] = ['A', 'A+', 'B', 'A', 'A+']

print(df)
