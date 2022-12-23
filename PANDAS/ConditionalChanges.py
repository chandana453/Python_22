import pandas as pd
df=pd.read_csv('Modified.csv')
#print(df)

#CONDITIONAL CHANGES

#CHanging the type1 of fire to flamer
df.loc[df['Type 1'] == 'Fire','Type 1']='Flamer'
#print(df)

#IF df['Type 1'] == 'Fire' change the type1 column that contains fire as "FLAMER"


#TO CHANGE IT BACK TO FLAMER, make slight changes
df.loc[df['Type 1'] == 'Flamer','Type 1']='Fire'
#print(df)

#To make all the Fire elements as True
df.loc[df['Type 1'] == 'Fire' ,'Legendary'] =True
#print(df)


df=pd.read_csv('Modified.csv')
#print(df)


#Multiple changes -> values > 500 ,replaces as "test value" in legendary column
df.loc[df['Total'] > 500,['Generation','Legendary']]= 'TEST VALUE'
#print(df)

df.loc[df['Total'] > 500,['Generation','Legendary']]= ['TEST 1' , 'TEST 2']
#print(df)

#TO CHECK THE ORIGINAL FILE WITH NO CHANGES MADE TO IT
df=pd.read_csv('Modified.csv')
print(df)