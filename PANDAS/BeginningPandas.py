#loading data into pandas

import pandas as pd
#df is dataframe
df=pd.read_csv('pokemon_data.csv')
print(df)

#******to load top and bottom of data of first 3 and last 3
# print(df.head(3))
# print(df.tail(3))

#*******to load excel file

#df_xlsx=pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head(3))


#***to load txt file
df=pd.read_csv('pokemon_data.txt',delimiter='\t')
#print(df.head(5))

#*********************READING DATA In PANDAS

print(df.columns)   #read headers

#********************Reading each column

#print("Reading each column")

#print(df['Name'])
#print(df['Name'][0:5])  #First 5 names
#print(df.Name)
#print(df[['Name','Type 1','HP']])

#**************************Reading each row

print("Reading each row")

#print(df.head(4))
#print(df.iloc[1])  #iloc() - integer location (returns everything in the first row)
#print(df.iloc[1:4])  # returns from index 1 to index 4

# for index,row in df.iterrows():
#     #print(index,row)
#     print(index, row['Name'])


#below line returns all the data where type1==grass

#print(df.loc[df['Type 1'] == "Grass"]) #finding specific data in our dataset that isn't just int based ,can based on numerical or text



#***********************Read a specific location(R,C)

#print("Read a specific location(Rows,Columns)")
#print(df.iloc[2,1])  # returns 2nd row 1st element

#DESCRIBE DATA
#print("Describe DATA")

#print(df.describe())  #gives count,mean,std,min etc

#**************************Sorting Values
#print("Sorting values by names")
#print(df.sort_values('Name'))

#print(df.sort_values('Name',ascending=False))
#print(df.sort_values(['Type 1','HP']))
#print(df.sort_values(['Type 1','HP'],ascending=[1,0]))

#ascending=[1,0] means 1 (Type 1 goes from low to high(ascending)) and HP from high to low(descending)

#**********************TO LOOK AT OUR DATA
#print(df.head(5))


#***********************ADDING NEW COLUMN CALLED "TOTAL"

df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
#print(df.head(5))  #new column(Total) is added at the last

#************Drop A Specific COlumn

#df=df.drop(columns=['Total'])
#print(df)

df['Total']=df.iloc[:,4:10].sum(axis=1)
#df.iloc[:, 4:10] -> first : means all rows everything -> 4:10 columns from index 4 to 9
#sum(axis=1) -> using sum() if axis=1, adding(sum) elements horizontally if axis=0 ,adding vertically

#*********To get columns as a list
cols = df.columns.values
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
#print(df.head(5))


#***********saving our data
##******To save it in CSV format

#df.to_csv('Modified.csv')  #saving our modified data in new file name modified.csv

#df.to_csv('Modified.csv',index=False) #Removing the index column from the file

#******To save it in EXCEL format

#df.to_excel('modified.xlsx',index=False)


#******To save it in TXT format
#df.to_csv('modified.txt',index=False, sep='\t')
