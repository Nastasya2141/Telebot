import telebot

token = '6176451589:AAGoruu-rXE5meMPofI1lrADptwuGCZSBbQ'
bot = telebot.TeleBot(token)

def send_answer(id,task,answer):
    bot.send_message(id, f'{task}\n {answer}')

data = open('tasks.txt', mode = 'r', encoding = 'utf-8')
tasks_list = data.readlines()
data.close()

answered_tasks = []
for row in tasks_list:
    split_row = row.split('!!')
    print(split_row)
    id = split_row[0]
    task = split_row[1]
    print(task[:-1])
    answer = input("Ответ ")
    send_answer(id, task, answer)

data = open('tasks.txt', mode = 'w', encoding = 'utf-8')
data.writelines(tasks_list)
data.close()
