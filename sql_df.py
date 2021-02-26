import sql_connection
import pandas as pd


writer = pd.ExcelWriter('C:\\Users\\Dmich\\Desktop\\output.xlsx', engine='xlsxwriter')

sql_connection.df.to_excel(writer, 'Sheet1')

writer.save()