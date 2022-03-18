from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import telebot
import os
from telebot import types
import user_agent
import osPORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["TOKEN"]
API_ENDPOINT = 'https://dog.ceo/api/breeds/image/random'

bot = telebot.TeleBot(token)

#Thanks For ZED Developer For IDea :)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi,\n=== === ===\nSend Your Name To Make it Gif!\n=== === ===\nBy : @trprogram</strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def mgit(message):
    text = message.text
    url = 'https://cooltext.com/PostChange'
    headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9',
               'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://cooltext.com',
               'referer': 'https://cooltext.com/Logo-Design-Animated-Glow', 'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'sec-gpc': '1',
               'user-agent': user_agent.generate_user_agent(), 'x-requested-with': 'XMLHttpRequest'}
    data = {
        'LogoID': '26',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo1 = (r.json()['renderLocation'])
    data = {
        'LogoID': '4',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo2 = (r.json()['renderLocation'])
    data = {
        'LogoID': '819721038',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo3 = (r.json()['renderLocation'])
    data = {
        'LogoID': '1169711118',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo4 = (r.json()['renderLocation'])
    data = {
        'LogoID': '819515844',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo5 = (r.json()['renderLocation'])
    data = {
        'LogoID': '790967832',
        'Text': f'{text}',
        'FontSize': '120',
        'Color1_color': '#000000', 'Color2_color': '#FFFFFF', 'Color3_color': '#000000',
        'Integer9': '0', 'Integer13': 'on', 'Integer12': 'on',
        'BackgroundColor_color': '#FFFFFF'
    }
    r = requests.post(url, headers=headers, data=data)
    logo6 = (r.json()['renderLocation'])
    bot.send_video(message.chat.id,logo1)
    bot.send_video(message.chat.id,logo2)
    bot.send_video(message.chat.id,logo3)
    bot.send_video(message.chat.id,logo4)
    bot.send_video(message.chat.id,logo5)
    bot.send_video(message.chat.id,logo6)
    bot.send_message(message.chat.id,f"Done!")
    pass
bot.polling()
