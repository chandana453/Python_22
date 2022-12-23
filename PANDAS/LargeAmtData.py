import pandas as pd

df=pd.read_csv('Modified.csv')

new_df=pd.DataFrame(columns=df.columns)

#we can read large amount of data into chunks of 5 rows each

for df in pd.read_csv('Modified.csv',chunksize=5):
  # print("CHUNK DATAFRAME")
  # print(df)
  results=df.groupby(['Type 1']).count()

  new_df=pd.concat([new_df,results])

print(new_df)