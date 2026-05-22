from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:pk252914@localhost:3306/pooja_medical')

df = pd.read_sql("SELECT * FROM users", engine)
print(df)
