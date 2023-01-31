import telebot
import time


bot = telebot.TeleBot("5953159365:AAHbB40ATCR-Zw6nMBKEphiam62l9ejIpIY")


@bot.message_handler(commands=['startSending'])
def start(message):
    pics_value = 0

    while pics_value <= 6:

        # отправляем картинку
        cat_photo = open(f"ParserPics/images{pics_value}.jpg", 'rb')
        bot.send_photo(message.chat.id, cat_photo)

        # задержка + переключение картинки
        pics_value += 1
        time.sleep(14400)


bot.polling(none_stop=True)
