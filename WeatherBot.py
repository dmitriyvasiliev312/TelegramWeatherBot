import requests
from bs4 import BeautifulSoup as b 
import telebot
API_KEY = '5240379159:AAEooGLe4oPkfLevwyrY4WvdZFKUXagpWTc'

def parser():
    URL = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2'
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    ttoday_temp = soup.find('p', class_='today-temp')
    today_temp = [c.text for c in ttoday_temp]
    tdescription = soup.find_all('div', class_='description')
    description = [c.text for c in tdescription]
    description.pop(2)
    tsunrise_sunset = soup.find('div', class_='infoDaylight')
    ttsunrise_sunset = tsunrise_sunset.find_all('span') 
    sunrise_sunset = [c.text for c in ttsunrise_sunset]
    weather = today_temp + description
    fweather = weather + sunrise_sunset
    return fweather
weather = parser()
print(parser())

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['weather'])
def welcome(message):
    bot.send_message(message.chat.id, weather[0])
    bot.send_message(message.chat.id, weather[2])
    bot.send_message(message.chat.id, weather[1])
    bot.send_message(message.chat.id, f'Время восхода: {weather[3]}, время заката: {weather[4]}.')
bot.polling()