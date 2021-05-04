import telebot
import pandas as pd
import sql_connection
import datetime
import sqllite
import sql_df

times = datetime.datetime.now()

token = '1660932890:AAHXbNz9JQIpiGAU6eGoSaSkeMzd6P_fFqI'
bot = telebot.TeleBot(token)


# подключение к локальной базе, check_same_thread=False без этого параметра ошибка трэда


# Бот реагирует на любое сообщение и предлагает ввести id для запроса в БД.
@bot.message_handler(func=lambda message: True)
def start_handler(message):
    chat_id = message.chat.id
    # text = message.text
    msg = bot.send_message(chat_id, 'Введите id пользователя')
    bot.register_next_step_handler(msg, id_client)


# Основная функция, нужно бить на части, слишком большая
def id_client(message):
    chat_id = message.chat.id
    global text
    text = message.text
    try:
        if not text.isdigit():  # Проверка что запрос типа int
            msg = bot.send_message(chat_id, 'id не может быть текстом. Введите число')
            bot.register_next_step_handler(msg, id_client)
            sqllite.update_sql(message.from_user.id, text, times)
            return
    except AttributeError:
        msg = bot.send_message(chat_id, 'Не правильный запрос.Введите число.')
        bot.register_next_step_handler(msg, id_client)
        sqllite.update_sql(message.from_user.id, text, times)
        return
    global user
    user = message.from_user.id
    print(message.from_user.id)  # id пользователя для записи в базу
    global df
    df = pd.read_sql_query(f"SELECT TOP 10*  FROM [3].[Customers] WHERE TSC_Customer_ID = {text} ",
                           sql_connection.cnxn)  # sql запрос в DataFrame
    writer = pd.ExcelWriter('C:\\Users\\Dmich\\Desktop\\output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, 'Sheet1')
    writer.save()
    doc = open('C:\\Users\\Dmich\\Desktop\\output.xlsx', 'rb')
    bot.send_document(message.chat.id, doc)  # Отправка excel обратно пользователю в чат
    sqllite.update_sql(user, text, times)  # Запись логов на локалку


# def save_link(message):
#     sql_connection.read_sql(sql_connection.cnxn)
#     sql_df.save_sql(df)
#     doc = open('C:\\Users\\Dmich\\Desktop\\output.xlsx', 'rb')
#     bot.send_document(message.chat.id, doc)
#     # bot.send_document(message.chat.id, "FILEID")
#     # bot.send_message(message.chat.id, "Сохранил!")


bot.polling()
# bot.polling(none_stop=False, interval=0, timeout=20)
