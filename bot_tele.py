import telebot
import pandas as pd
import sql_connection
import sql_df
token = '1660932890:AAHXbNz9JQIpiGAU6eGoSaSkeMzd6P_fFqI'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Укажите id пользователя, по которому хотите получить данные')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(message.text)
    # // вывод сообщения которое написал пользователь
    sent = bot.send_message(message.chat.id, "Укажите id пользователя, по которому хотите получить данные:")
    bot.register_next_step_handler(sent, save_link)

def save_link(message):
    global id_client
    id_client = message.text
    df = pd.read_sql_query(f"SELECT TOP 10*  FROM [3].[Customers] WHERE TSC_Customer_ID = {id_client} ", sql_connection.cnxn)
    writer = pd.ExcelWriter('C:\\Users\\Dmich\\Desktop\\output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, 'Sheet1')
    writer.save()
    doc = open('C:\\Users\\Dmich\\Desktop\\output.xlsx', 'rb')
    bot.send_document(message.chat.id, doc)
    # bot.send_document(message.chat.id, "FILEID")
    # bot.send_message(message.chat.id, "Сохранил!")


bot.polling()
# bot.polling(none_stop=False, interval=0, timeout=20)