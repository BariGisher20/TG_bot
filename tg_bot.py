import telebot
from telebot import types
from config import token
# from telegram.ext import Updater, CommandHandler
# import request


token = token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')  # для обращения к боту и определения его действий надо обращаться через bot.
# через message.chat.id мы получаем именно тот чат, откуда получили сообщение


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, 'You are welcome!', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f"Your id: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('me.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'What?', parse_mode='html')

# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()  # InlineKeyboardMarkup - встроенные в сообщения элементы (не только кнопки)
#     markup.add(types.InlineKeyboardButton("Go to WEB-site", url="https://vk.com/bari_gisher19"))
#     bot.send_message(message.chat.id, "Bari Gisher", reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  # InlineKeyboardMarkup - встроенные в сообщения элементы (не только кнопки)
    website = types.KeyboardButton('WEB-site')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, "Bari Gisher", reply_markup=markup)


bot.polling(none_stop=True)
