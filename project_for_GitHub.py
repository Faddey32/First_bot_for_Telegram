import telebot

bot = telebot.TeleBot('your-key')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == 'привет':
        answer = 'привет, как я могу помочь?'
        bot.send_message(message.from_user.id, answer)
    elif message.text == '/help':
        answer = 'Напиши привет'
        bot.send_message(message.from_user.id, answer)
    else:
        answer = 'я вас не понимаю'
        bot.send_message(message.from_user.id, answer)

bot.polling(none_stop=True, interval=0)