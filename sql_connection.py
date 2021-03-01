import pandas as pd
import pyodbc
import bot_tele

server = 'SQL.Samorodov.SU'
database = '(лаб) Банк Олега Тинькова (TCS)'
username = 'Чуркин Дмитрий Юрьевич'
password = 'Dima070193'

cnxn = pyodbc.connect(
    'DRIVER={SQL Server Native Client 11.0};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
with cnxn:
    cursor = cnxn.cursor()



def read_sql(connect):
    a = bot_tele.id_client
    df = pd.read_sql_query(f"SELECT TOP 10*  FROM [3].[Customers] WHERE TSC_Customer_ID = {a} ", connect)
    print(df)
    return df


pyodbc.pooling = False

