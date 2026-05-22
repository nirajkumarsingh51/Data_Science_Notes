import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('bihar_groundwater.csv')
# Display the first few rows of the dataset
print(df.head())

df.info()
df.describe().round()

df.isnull().sum()/len(df) * 100

# df.shape