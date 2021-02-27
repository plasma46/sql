import telebot
import pandas as pd
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
    doc = open('C:\\Users\\Dmich\\Desktop\\output.xlsx', 'rb')
    bot.send_document(message.chat.id, doc)
    # bot.send_document(message.chat.id, "FILEID")
    # bot.send_message(message.chat.id, "Сохранил!")



bot.polling()