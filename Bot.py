import telebot
import time

bot = telebot.TeleBot("5953159365:AAG5dKZk_4kNFDq0UzjrdvZhHYgp4xD1gO4")

pics_value = 242


@bot.message_handler(commands=['startSending'])
def start(message):
    steps = 0

    while steps <= pics_value:
        # отправляем картинку
        cat_photo = open(f"ParserPics/images{steps}.jpg", 'rb')
        bot.send_photo(message.chat.id, cat_photo)

        # задержка + переключение картинки
        steps += 1
        time.sleep(14400)


@bot.message_handler(commands=['globalStop'])
def stop(message):
    bot.send_message(message.chat.id, "Бот остановлен!")
    bot.stop_bot()


bot.polling(none_stop=True)
