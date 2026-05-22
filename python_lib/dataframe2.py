import pandas as pd

data = [[ 'Niraj', 22, 80],
        ['Suman', 25, 40],
        ['Rohit', 55, 22],
        ['Sita', 25, 50],
]

df = pd.DataFrame(data,
                  columns=['Name', 'Age', 'Marks']
                  )

print(data)
print(df)