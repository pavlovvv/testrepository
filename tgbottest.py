import telebot
bot = telebot.TeleBot('1647323491:AAGXEpzue4uSEEWAO5V5oNilMbUR8DjFtfo')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'ку':
        bot.send_message(message.from_user.id, 'кударова')
    else:
        bot.send_message(message.from_user.id, 'че')
bot.polling(none_stop=True)
