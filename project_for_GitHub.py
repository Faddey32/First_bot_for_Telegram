import telebot
from your_key import key

bot = telebot.TeleBot(key)

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == 'привет':
        answer = 'привет, как я могу помочь?'
        bot.send_message(message.from_user.id, answer)
    elif message.text == '/help':
        answer = 'Напиши привет'
        bot.send_message(message.from_user.id, answer)
    elif message.text == '/check-GitHub':
        response = r.get('https://github.com')
        if response.status_code == 200:
            bot.send_message(message.from_user.id, 'Доступен')
        else:
            bot.send_message(message.from_user.id, 'недоступен')
    else:
        answer = 'я вас не понимаю'
        bot.send_message(message.from_user.id, answer)

bot.polling(none_stop=True, interval=0)