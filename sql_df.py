import sql_connection
import pandas as pd


def save_sql(data):
    writer = pd.ExcelWriter('C:\\Users\\Dmich\\Desktop\\output.xlsx', engine='xlsxwriter')
    data.to_excel(writer, 'Sheet1')
    writer.save()
