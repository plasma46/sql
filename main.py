import pandas as pd
import pyodbc

server = 'SQL.Samorodov.SU'
database = '(лаб) Банк Олега Тинькова (TCS)'
username = 'Чуркин Дмитрий Юрьевич'
password = 'Dima070193'

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
a = int(input('Введите значения '))

df = pd.read_sql_query(f"SELECT TOP 10*  FROM [3].[Customers] WHERE TSC_Customer_ID = {a} ",cnxn)
print(df)

pyodbc.pooling = False

