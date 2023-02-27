# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения 
# пользователей в файл.
import telebot

token = '6176451589:AAGoruu-rXE5meMPofI1lrADptwuGCZSBbQ'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Здравствуйте! Я бот технической поддержки, опишите вашу проблему")

@bot.message_handler(content_types= ['text'])
def read_text_commands(message):
        data = open('tasks.txt', mode = 'a', encoding = 'utf-8')
        data.writelines(f'{message.from_user.id}!!{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n')
        data.close()
        bot.reply_to(message, "Ваш вопрос отправлен в техподдержку.")


bot.infinity_polling()