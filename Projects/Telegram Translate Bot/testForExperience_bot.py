import telebot
import random
import datetime
from googletrans import Translator

# Токен бота
TOKEN = '1255957265:AAEBX6aHy4DqnNHrCExFYl700h2pbTs-Bhc'

# Токен api переводчика
TOKEN_TRANSLATER = 'NGMyNTNhZWUtYWM5Yy00ZGVhLWIxZTItYTJhNmQ5ZjI2YWY3OmM4NWQ0NTk3OWMwODRjMDE5NTg1YWU0MjZmYzQ2ZWZi'

# Объект для переводчика
translator = Translator()

# Доступ к боту
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def main(m):
    if m.text == 'Привет':
        bot.send_message(m.chat.id, m.text + ' ' + m.from_user.first_name)

    elif m.text == 'Ты как?':
        answer_list = ['Нормально', 'Отлично', 'Сойдёт', 'Лучше всех среди ботов']
        answer = random.choice(answer_list)
        bot.send_message(m.chat.id, answer)

    elif m.text == 'Что делаешь?':
        answer_list = ['Ничего', 'Отдыхаю', 'Ем', 'Работаю']
        answer = random.choice(answer_list)
        bot.send_message(m.chat.id, answer)

    elif m.text == 'Время':
        time = datetime.datetime.today().strftime("%H:%M")
        bot.send_message(m.chat.id, time)

    else:
        text = m.text
        bot.send_message(m.chat.id, translate(text))

# Перевести текст
def translate(text):
    result = translator.translate(text)
    return result.text


# Зациклить работу скрипта
if __name__ == '__main__':
    bot.polling(none_stop=True)