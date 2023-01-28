from telebot import TeleBot


TOKEN = '1084443519:AAHw8kZ3RjfYZBYRASHH6A5pGle-VUa5yCM'
bot = TeleBot(TOKEN)



@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Привет!')



@bot.message_handler(content_types=['text'])
def get_text_message(message):
	bot.send_message(message.from_user.id, message.text)



bot.polling(none_stop=True, interval=0)