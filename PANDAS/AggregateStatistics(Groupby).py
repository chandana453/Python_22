import pandas as pd

df=pd.read_csv('Modified.csv')

#groupby function

#df=df.groupby(['Name']).mean().sort_values('Attack', ascending=False)
#print(df)

#df=df.groupby(['Type 1']).sum()
#print(df)

df['count']=1
#df1=df.groupby(['Type 1']).count()
#print(df)


df1=df.groupby(['Type 1']).count()['count']
print(df1)

# df1=df.groupby(['Type 1','Type 2']).count()['count']
# print(df1)