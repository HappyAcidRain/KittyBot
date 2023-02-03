# для постоянной работы
import os
import sys
from requests.exceptions import ConnectionError, ReadTimeout

# для прочего
from random import randint
import telebot
import time
import datetime

bot = telebot.TeleBot("5953159365:AAG5dKZk_4kNFDq0UzjrdvZhHYgp4xD1gO4")

# количество зарегистрированных изображений
pics_value = 244


# актуальное время
def curTime():
    current_date = datetime.datetime.now()

    # Retrieving each component of the date
    # i.e year,month,day,hour,minute,second and
    # Multiplying with multiples of 100
    # year - 10000000000
    # month - 100000000
    # day - 1000000
    # hour - 10000
    # minute - 100

    current_time = current_date.hour * 100 + current_date.minute
    return current_time


# рассылка картинок (задержка: 4 часа)
@bot.message_handler(commands=['startSending'])
def start(message):
    steps = randint(0, pics_value)

    while steps <= pics_value:
        current_time = curTime()

        # c 8:00              до 23:00
        if 800 < current_time < 2300:
            # отправляем картинку
            cat_photo = open(f"ParserPics/images{steps}.jpg", 'rb')
            bot.send_photo(message.chat.id, cat_photo)

        else:
            # спатки
            pass

        # задержка + переключение картинки
        steps = randint(0, pics_value)
        time.sleep(14400)


# полная остановка
@bot.message_handler(commands=['globalStop'])
def stop(message):
    bot.send_message(message.chat.id, "Бот остановлен!")
    bot.stop_bot()


# проверка состояния
@bot.message_handler(commands=['statusCheck'])
def check(message):
    bot.send_message(message.chat.id, f"Бот работает \n Изображений в базе: {pics_value}")


# для постоянной работы
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
