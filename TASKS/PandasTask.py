import pandas as pd
from psycopg2 import sql

#1.fetch the input csv file from local

import csv

#with open("/Users/mounika/PycharmProjects/PANDAS/pokemon_data.csv",'r') as file:
    # for data in file:
    #     csvreader = csv.reader(file)  # importing the csv library in order to use the .reader() method it contains to help us read the csv file.
    #     for row in csvreader:
    #         print(row)


#2-read the csv file by using pandas

df= pd.read_csv("/PANDAS/pokemon_data.csv")
# print(df.head(5))

#3.insert the data frame into db

from sqlalchemy import create_engine

username = 'postgres'
password = 'm'
hostname = 'localhost'
port = 5432
dbname = 'users'

# A long string that contains the necessary Postgres login information
postgres_str = f'postgresql://{username}:{password}@{hostname}:{port}/{dbname}'

#Create the connection
conn = create_engine(postgres_str)

#Loading your pandas dataframe into your SQL db as a table
df= pd.read_csv("/PANDAS/pokemon_data.csv")
df.to_sql('Pokemon_DATA', con=conn, index=False)   #Pokemon_DATA is a table name




#*********ANOTHER WAY********


#
# from sqlalchemy import create_engine as ce
# import pandas as pd
#
# df1=pd.read_excel("C:\\Users\\lenovo\\Desktop\\Chandra.xlsx",sheet_name="missing data")
#
# A=ce("postgresql://postgres:ravichandra@localhost:5432/sekhar")
# df1.to_sql("missing_data", A)


#source:https://blog.panoply.io/how-to-load-pandas-dataframes-into-sql

