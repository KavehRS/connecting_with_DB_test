# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


