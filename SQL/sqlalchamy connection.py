import sqlalchemy

# What is SQLAlchemy library?
# SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL
# SQLAlchemy is a library that facilitates the communication between Python programs and databases.

import psycopg2
from sqlalchemy import create_engine as ce
import pandas as pd
#
a=pd.read_excel("C:\\Users\\lenovo\\Desktop\\Chandra.xlsx",sheet_name="missing data")

A=ce("postgresql://postgres:ravichandra@localhost:5432/sekhar")
a.to_sql("missing_dat", A)

