from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import osPORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ["TOKEN"]
API_ENDPOINT = 'https://dog.ceo/api/breeds/image/random'
