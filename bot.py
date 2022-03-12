import telebot
from telebot import types

import configure

bot = telebot.TeleBot(configure.config['token'])


#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Здравствуйте! Вы Хотите Записать Свой Ноут На Мастер Класс?")


@bot.message_handler(commands=['start'])
def start_message(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='Не', callback_data='no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Здравствуйте! Вы Хотите Записать Свой Ноут На Мастер Класс?",
                     reply_markup=markup_inline
                     )


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Ваше Фамилия и Имя")
        bot.send_message(call.message.chat.id, "Направление")
        bot.send_message(call.message.chat.id, "Количество")
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Ладно, пока")
        bot.send_message(call.message.chat.id, "👋🏻")


bot.polling(non_stop=True, interval=0)
