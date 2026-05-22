import pandas as pd

#data = pd.Series([1, 2, 3, 4, 5])
data = pd.Series([80, 90, 75, 85, 95], 
index=['Niraj', 'Suman', 'Rohit', 'Sita', 'Gita'])
print(data['Niraj'])  # Accessing element by index

marks = pd.Series([80, 90, 75, 85, 95])
print(marks + 5)
print(marks * 2)