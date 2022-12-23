from sqlalchemy import create_engine

import pandas as pd

df=pd.read_csv("/Users/mounika/Desktop/employees_data.txt",delimiter='\t')
conn=create_engine("postgresql://postgres:m@localhost:5432/users")
df.to_sql('Employees', con=conn, index=False)

