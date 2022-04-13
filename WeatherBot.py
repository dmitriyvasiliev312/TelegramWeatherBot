import requests
from bs4 import BeautifulSoup as b 
import telebot
API_KEY = '5240379159:AAEooGLe4oPkfLevwyrY4WvdZFKUXagpWTc'
URL = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2'

def current_weather(url):   
    r = requests.get(url)
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
    return weather + sunrise_sunset
def week_forecast(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    tminweek_forecast = soup.find_all('div', class_='min')
    tmaxweek_forecast = soup.find_all('div', class_='max')
    minweek_forecast = [c.text for c in tminweek_forecast]
    maxweek_forecast = [c.text for c in tmaxweek_forecast]
    return maxweek_forecast + minweek_forecast
def date(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')    
    tday = soup.find_all('p', class_='date')
    tmonth = soup.find_all('p', class_='month')
    tdate = tday + tmonth
    return [c.text for c in tdate]
def today_forecast(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    ttoday_forecast = soup.find('tr', class_='temperature')
    tttoday_forecast = ttoday_forecast.find_all('td')
    return [c.text for c in tttoday_forecast]

weather = current_weather(URL)
date_list = date(URL)
week_forecast_list = week_forecast(URL)
today_forecast_list = today_forecast(URL)
print(current_weather(URL))
print(week_forecast(URL))
print(date(URL))
print(today_forecast(URL))

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['weather'])
def today_weather_message(message):
    bot.send_message(message.chat.id, weather[0])
    bot.send_message(message.chat.id, weather[2])
    bot.send_message(message.chat.id, weather[1])
    bot.send_message(message.chat.id, f'Время восхода: {weather[3]}, время заката: {weather[4]}.')
@bot.message_handler(commands=['weekforecast'])
def week_forecast_message(message):
    bot.send_message(message.chat.id, f'{date_list[0]} {date_list[7]}: {week_forecast_list[7]}, {week_forecast_list[0]}.')
    bot.send_message(message.chat.id, f'{date_list[1]} {date_list[7]}: {week_forecast_list[8]}, {week_forecast_list[1]}.')
    bot.send_message(message.chat.id, f'{date_list[2]} {date_list[7]}: {week_forecast_list[9]}, {week_forecast_list[2]}.')
    bot.send_message(message.chat.id, f'{date_list[3]} {date_list[7]}: {week_forecast_list[10]}, {week_forecast_list[3]}.')
    bot.send_message(message.chat.id, f'{date_list[4]} {date_list[7]}: {week_forecast_list[11]}, {week_forecast_list[4]}.')
    bot.send_message(message.chat.id, f'{date_list[5]} {date_list[7]}: {week_forecast_list[12]}, {week_forecast_list[5]}.')
    bot.send_message(message.chat.id, f'{date_list[6]} {date_list[7]}: {week_forecast_list[13]}, {week_forecast_list[6]}.')
@bot.message_handler(commands=['todayforecast'])
def today_forecast_message(message):
    bot.send_message(message.chat.id, f'0:00 : {today_forecast_list[0]}')
    bot.send_message(message.chat.id, f'3:00 : {today_forecast_list[1]}')
    bot.send_message(message.chat.id, f'6:00 : {today_forecast_list[2]}')
    bot.send_message(message.chat.id, f'9:00 : {today_forecast_list[3]}')
    bot.send_message(message.chat.id, f'12:00 : {today_forecast_list[4]}')
    bot.send_message(message.chat.id, f'15:00 : {today_forecast_list[5]}')
    bot.send_message(message.chat.id, f'18:00 : {today_forecast_list[6]}')
    bot.send_message(message.chat.id, f'21:00 : {today_forecast_list[7]}')
bot.polling() 
