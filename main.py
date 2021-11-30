# Kaveh RezaeiShiraz @KavehRS
# pyodbc_test with db


## pyodbc_test with sqlserver
import pyodbc
import pandas as pd
vod_str = ("Driver={SQL Server Native Client 11.0};"
            "Server= 192.168.200.36, 1433;"
            "Database=VOD;"
            "UID=kaveh;"
            "PWD=*********;")
vod = pyodbc.connect(vod_str)


# Initialise the Cursor


cursor = vod.cursor()
cursor.execute('SELECT * FROM DB1_VOD')
records = cursor.fetchall()
db1_VOD = []
columnNames = [column[0] for column in cursor.description]
for record in records:
    db1_VOD.append( dict( zip( columnNames , record ) ) )
db1_VOD = pd.DataFrame(db1_VOD)




## pyodbc_test with psql
import psycopg2
import pandas.io.sql as psql
connection = psycopg2.connect(user="***********",
                                    password="**********",
                                    host="10.32.141.17",
                                    port="5432",
                                    database="**********")
cursor = connection.cursor()
df= psql.read_sql("SELECT * FROM public.web_metatest0", connection)
print(len(df))




from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:****password****@10.32.141.17/kaveh',pool_size=20, max_overflow=100,)
con=engine.connect()
sarasari.to_sql('sarasari',con,if_exists='append', index=False)
con.close()
