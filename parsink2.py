from hashlib import new
from types import new_class
from bs4 import BeautifulSoup
import requests
from telebot import types
import telebot
import random

TOKEN = '5046178054:AAHuQwkWDCf-xdFs1QK09ywTKwulBEGR8E8' # @raigorodok_bot


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    Button1 = types.KeyboardButton('Погода🌤')
    Button2 = types.KeyboardButton('Новости📣')
    Button3 = types.KeyboardButton('Информация📡')
    markup.add(Button1, Button2, Button3)

    user_name = message.from_user.full_name

    bot.send_message(message.chat.id, f'{user_name}, добро пожаловать в бота "СМИ Райгородка"!👋',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private' :
        if message.text == 'Информация📡' :
            

            user_name = message.from_user.full_name
            bot.send_message(message.chat.id, f'{user_name} , разработчиком этого бота являеться @varseev_fx ☺️')


        if message.text == 'Новости📣' :
            url = 'https://news.meta.ua/metka:райгородок/'
            
            page = requests.get(url)
            
            soup = BeautifulSoup(page.text, 'html.parser')
            new_news = []
            news = soup.find_all('div', class_='one-news-cnt')

            user_name = message.from_user.full_name

            bot.send_message(message.chat.id, f'{user_name}, вот все новости Райгородка🔔' )

            for data in news:
                data_url = data.get('href')
                bot.send_message(message.chat.id,f'{data.text}🔈')

        if message.text == 'Погода🌤' :
            url = 'https://sinoptik.ua/погода-райгородок-303022550'

            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'html.parser')

            pogoda = []

            pogoda1 = soup.find('p', class_='today-temp')

            pogoda_min = soup.find('div', class_='min').find('span')        
            pogoda_max = soup.find('div', class_='max').find('span')  
            data = soup.find('p', class_='date')
            month = soup.find('p', class_='month')
            infoDaylight = soup.find('div', class_='infoDaylight')

            bot.send_message(message.chat.id,'\n🔍Дата: '+ data.text + month.text +' \n\n⛅️На данный момент погода в смт.Райгородок: ' + pogoda1.text + '\n\nПодробная информация о погоде☀️\n🌚Минимум: ' + pogoda_min.text + '\n🌝Максимум: ' + pogoda_max.text + '\n\n⌛️'+ infoDaylight.text )




bot.polling(none_stop= True)