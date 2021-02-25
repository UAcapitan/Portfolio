import telebot
import random
import datetime
import pymysql
import httplib2
import googleapiclient.discovery
from pymysql.cursors import DictCursor
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
from googletrans import Translator

# Токен бота
TOKEN = '1255957265:AAEBX6aHy4DqnNHrCExFYl700h2pbTs-Bhc'

# Токен api переводчика
TOKEN_TRANSLATER = 'NGMyNTNhZWUtYWM5Yy00ZGVhLWIxZTItYTJhNmQ5ZjI2YWY3OmM4NWQ0NTk3OWMwODRjMDE5NTg1YWU0MjZmYzQ2ZWZi'

# Подключение к базе данных
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='prog',
    charset='utf8mb4',
    cursorclass=DictCursor
)

# Создание курсора
cursor = connection.cursor()

# fileCreds = 'creds.json'
# creds_id = '17tYQzae5JzoiuSoTsQNwBInnQmod1z-IRKSypuGduPM'

# cr = ServiceAccountCredentials.from_json_keyfile_name(
#     fileCreds,
#     ['https://www.googleapis.com/auth/spreadsheets',
#     'https://www.googleapis.com/auth/drive'])
# httpAuth = cr.authorize(httplib2.Http())
# service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

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

    elif m.text == 'Покажи прикол':
        bot.send_photo(m.chat.id, get_db_image())

    elif m.text == 'Покажи таблицу':
        get_sheet()

    elif "Перевести:" in m.text:
        text = m.text
        text = text.replace('Перевести:', '')
        bot.send_message(m.chat.id, translate(text))

    else:
        text = m.text
        bot.send_message(m.chat.id, search_in_google(text))

# Выгрузка фото с базы данных
def get_db_image():

    # Запрос данных в базу
    cursor.execute('SELECT image FROM imageURL ORDER BY id DESC LIMIT 1')
    info = cursor.fetchall()

    # Возврат результата
    return info[0]['image']

# Показать таблицу
def get_sheet():
    pass

# Поиск в гугле
def search_in_google(text):
    text = text.replace(' ', '+')
    site = 'https://www.google.ru/search?newwindow=1&hl=ru&sxsrf=ALeKk03mdhOYiqUeNsSMIj-2_H1j06vTtw%3A1596453991665&source=hp&ei=Z_QnX_elJoO-aLXptIgB&q=' + text
    return site

# Перевести текст
def translate(text):
    result = translator.translate(text)
    return result.text


# Зациклить работу скрипта
if __name__ == '__main__':
    bot.polling(none_stop=True)