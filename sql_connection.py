# import pyodbc
# import pandas as pd
#
# # writer = pd.ExcelWriter('C:\\Users\\dmchurkin\\Desktop\\output.xlsx', engine='xlsxwriter')
#
# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
# "Server=localhost;"
# "Database=AdventureWorks2008R2;"
# "Trusted_Connection=yes;")
#
# a = int(input('Введите значения'))
#
# cursor = cnxn.cursor()
#
# df = pd.read_sql_query(f"SELECT TOP 10*  FROM [AdventureWorks2008R2].[Sales].[Customer] WHERE CustomerID = {a} ",cnxn)
# print(df)
#
# df.to_excel(writer, 'Sheet1')
#
# writer.save()
# ```
import pandas as pd
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'SQL Samorodov SU'
database = '(лаб) Банк Олега Тинькова (TCS)'
username = 'Чуркин Дмитрий Юрьевич'
password = 'Dima070193'
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

a = int(input('Введите значения'))

df = pd.read_sql_query(f"SELECT TOP 10*  FROM [3].[Customers] WHERE TSC_CustomerID = {a} ",cnxn)
print(df)