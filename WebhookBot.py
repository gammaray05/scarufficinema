from flask import Flask, request
import requests
import telepot
import pandas as pd
import urllib3


proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "SECRET"
bot = telepot.Bot('TOKEN')
bot.setWebhook("https://gammaray05.pythonanywhere.com/{}".format(secret), max_connections=40)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()

    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]

        if text == "/best1910s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1910s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1920s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1920s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1930s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1930s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1940s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1940s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1950s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1950s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1960s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1960s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1970s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1970s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1980s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1980s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best1990s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1990s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best2000s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best2000s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"

        if text == "/best2010s":
            link = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best2010s.txt"
            f = requests.get(link)
            bot.sendMessage(chat_id, f.text)
            return "OK"


        if text == "/start":
            bot.sendMessage(chat_id, "Please, type a movie (English title) or a director to search ratings from scaruffi.com. Only movies from 1998 to present are listed. \n \nOr you can use commands like /best1980s, /best1970s, etc.. to retrieve the list of the best movies of a decade.\n \nSearch is case insensitive. For example, you can search: \nLynch \nallen \nAnderson \ngreat beauty \nYouth \n\n Developer: @salvdelg. You can find the git on https://bit.ly/2SSr9Fx" )
            return "OK"



        url="https://raw.githubusercontent.com/gammaray05/scarufficinema/master/list.csv"
        master = pd.read_csv(url, sep=',', names = ['RATING', 'DIRECTOR', 'MOVIE'])
        result = master[ master['DIRECTOR'].str.contains(text, case=False, regex=False) | master['MOVIE'].str.contains(text, case=False, regex=False) ]
        resultlist = result.values.T.tolist()
        zippedlist = list(zip(*resultlist))
        final = "\n".join([" - ".join(tup) for tup in zippedlist])
        if not final:
            bot.sendMessage(chat_id, "No results found. Check the title or the name. Please remember to use the English title of the movie and that only movies from 1998 to present are listed.")
            return "OK"
        else:
            bot.sendMessage(chat_id, final)
            return "OK"
