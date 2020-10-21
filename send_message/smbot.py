import telebot

#paste token here
token = 'token'

tb = telebot.TeleBot(token)
tb.send_message(00000000, "Введите сообщение")