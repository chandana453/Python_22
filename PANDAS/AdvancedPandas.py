import pandas as pd
#FILTERING DATA

df=pd.read_csv('pokemon_data.csv')
#print(df)

df=df.loc[df['Type 1'] == 'Grass']
#print(df)

##filtering data using and (&)
df=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2']=='Poison')]
#print(df)


#filtering data using or (|)

df=df.loc[(df['Type 1'] == 'Grass') | (df['Type 2']=='Poison')]
#print(df)

new_df=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]
#print(new_df)
new_df.to_csv('Filtered.csv',index=False) #saves the filtered data into a new file by removing index colu,n
#print(new_df) -> this print different indexes, to reset this use below

new_df = new_df.reset_index()  # it helps in resetting index in ascending order
#print(new_df)  # we see that it prints both old and new indexes

#in order to remove old indexes,use drop=True
new_df.reset_index(drop=True, inplace=True)
#print(new_df)

#prints the data that has the name "Mega" in it
df=pd.read_csv('pokemon_data.csv')
df1=df.loc[df['Name'].str.contains('Mega')]
#print(df1)


#prints the data that doesn't have the name "Mega" in it(using ~ operator)
df2=df.loc[~df['Name'].str.contains('Mega')]
#print(df2)

#print(df)


#USING REGULAR EXPRESSIONS

import re
df3=df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]
#print(df3)

df3=df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]   #re.I is ignore capitialization of fire and grass
#print(df3)


#GET ALL POKEMON NAMES with PI
df=df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(df)


#'^pi[a-z]*' - this helps in printing names starting (^) with pi and matching with any of chars[a-z] any times(*)


