from curses.panel import bottom_panel
from tokenize import Token
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import *
from TBOT.credentials import bot_token, bot_username, URL
import requests
import os


PORT = int(os.environ.get('PORT', 5000))

global bot
global TOKEN
TOKEN=bot_token

def get_Download_URL_From_API(url):
    API_URL = "https://getvideo.p.rapidapi.com/"
    querystring = {"url": f"{url}"}

    conn = http.client.HTTPSConnection("youtube-search-and-download.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "youtube-search-and-download.p.rapidapi.com",
        'X-RapidAPI-Key': "971ed126b4msh71440a93902ba14p159054jsn269737d77060"
    }

    conn.request("GET", "/video/related?id=" + querystring, headers=headers)

    res = conn.getresponse()
    data = res.read()

print(data.decode("utf-8"))


def start(update: Update, context: CallbackContext):
    update.message.reply_text(text='Welcome to URL downloader!\nPlease provide a valid url')

def textHandler(update: Update, context: CallbackContext) -> None:
    if update.message.parse_entities(types=MessageEntity.URL):
        update.message.reply_text(text='You sent a valid URL!', quote=True)

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, textHandler, run_async=True))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://prodigy8-bot.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()