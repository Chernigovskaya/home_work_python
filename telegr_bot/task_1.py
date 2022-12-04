import telebot
import requests
import time
import io
from telebot import types
from random import randint


number = 0
steps = 1
is_started = False
calc = False
result = 0


bot = telebot.TeleBot("5808394330:AAEa-Y3C1KadPsEcAvVzYJvaLFyKxDETChM", parse_mode=None)
markup = types.ReplyKeyboardMarkup(row_width=3) #сщздается клавиатура
itembtn1 = types.KeyboardButton('погода')
itembtn2 = types.KeyboardButton('котик')
itembtn3 = types.KeyboardButton('регистрация')
itembtn4 = types.KeyboardButton('играть')
itembtn5 = types.KeyboardButton('калькулятор')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
# bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(commands=['start', 'help', 'hello']) # Добавьте возможность рассылки напоминания всем зарегистрированным пользователям.
def send_welcome(message):
    bot.reply_to(message, 'привет, ' + message.from_user.first_name, reply_markup=markup)


@bot.message_handler(commands=['notify'])  # Добавьте возможность рассылки напоминания всем зарегистрированным пользователям.
def notify(message):
    data = open('users_id.txt', 'r', encoding='utf-8')
    users = data.readlines()
    for i in users:
        try:
            bot.send_message(i[:-1], 'оповещение')
        except telebot.apihelper.ApiTelegramException:
            print(f'Сообщение пользователю {i[:-1]} отправить не удалось')
    data.close()
    # print(message) #инфо о сообщении


@bot.message_handler(content_types=['text']) # если сообщение равно текст
def hello_user(message):
    global is_started
    global calc
    global number
    global steps
    global result
    if is_started:
        if message.text.isdigit():
            input_num = int(message.text)
            if input_num > number:
                bot.send_message(message.from_user.id, 'меньше')
            elif input_num < number:
                bot.send_message(message.from_user.id, 'больше')
            else:
                is_started = False
                bot.send_message(message.from_user.id, f'Ура!!! Вы угадали, я загадал число {number}. Тебе потребовалось {steps} ходов')
                steps = 0
            steps = steps + 1
        elif message.text == 'стоп':
            is_started = False
        else:
            bot.send_message(message.from_user.id, 'Введи число')
    elif calc:
        result = eval(message.text)
        bot.reply_to(message, f' ответ {result}')
        calc = False
        result = 0
    else:
        print(f'{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
        if 'привет' in message.text:
            bot.reply_to(message, 'привет, ' + message.from_user.first_name)

        elif message.text == 'играть':
            number = randint(1, 1001)
            is_started = True
            bot.reply_to(message, f'я загадал число от 1 до 1000, попробуй его отгадать. Введи число')
            bot.send_message(message.from_user.id, 'Для выхода введите "стоп"')

        elif message.text == 'погода':
            r = requests.get('https://wttr.in/?0T')
            bot.reply_to(message, r.text)

        elif message.text == 'калькулятор':
            calc = True
            bot.send_message(message.from_user.id, 'Введите выражение')

        elif message.text == 'котик':
            r = f'https://cataas.com/cat?t=${time.time()}'
            bot.send_photo(message.chat.id, r)

        elif message.text == 'файл': # переслать файл
            data = open('test.txt', encoding='utf-8')
            bot.send_document(message.chat.id, data)
            data.close()

        elif message.text == 'регистрация': # Добавьте боту возможность регистрации.
                                            # Добавьте команду, которая запишет id пользователя в файл.
            user_id = str(message.from_user.id) + '\n'
            data = open('users_id.txt', 'r+', encoding='utf_8')
            try:
                lines = data.readlines()
                if user_id not in lines:
                    data.writelines(str(message.from_user.id) + '\n')
                    bot.send_message(message.from_user.id, 'Регистрация прошла успешно!')
                else:
                    bot.send_message(message.from_user.id, 'Пользователь уже зарегистрирован!')

            except io.UnsupportedOperation:
                data.writelines(str(message.from_user.id) + '\n')
                bot.send_message(message.from_user.id, 'Регистрация прошла успешно')
            data.close()
        else:
            bot.send_message(message.from_user.id, 'Введите /start или /help')

        data = open('user_message.txt', 'a+', encoding='utf-8')
        data.writelines(str(message.from_user.id) + ' ' + message.text + '\n') # записывает сообщения в файл
        data.close()
        # bot.reply_to(message, message.text) #отвечает на сообщения пользователя тем же


bot.infinity_polling()
