from flask import Flask, request
import requests
import telebot
import pandas as pd
import os
import time

#initialize resources
url="https://raw.githubusercontent.com/gammaray05/scarufficinema/master/list.csv"
tsurl = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/timestamp.txt"
timestamp = requests.get(tsurl)
master = pd.read_csv(url, sep=',', header=0)
master.to_pickle('data.pkl')
df = pd.read_pickle('data.pkl')

#initialize commands
alltime = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/alltime.txt"
alltimet = requests.get(alltime)
dieci = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1910s.txt"
diecit = requests.get(dieci)
venti = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1920s.txt"
ventit = requests.get(venti)
trenta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1930s.txt"
trentat = requests.get(trenta)
quaranta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1940s.txt"
quarantat = requests.get(quaranta)
cinquanta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1950s.txt"
cinquantat = requests.get(cinquanta)
sessanta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1960s.txt"
sessantat = requests.get(sessanta)
settanta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1970s.txt"
settantat = requests.get(settanta)
ottanta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1980s.txt"
ottantat = requests.get(ottanta)
novanta = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best1990s.txt"
novantat = requests.get(novanta)
zerozero = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best2000s.txt"
zerozerot = requests.get(zerozero)
zerodieci = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/best%20by%20decades/best2010s.txt"
zerodiecit = requests.get(zerodieci)

#starting bot
TOKEN = os.environ["TOKEN"]
URL = os.environ["URL"]

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

#handle commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Please, type a movie (English title) OR a director to search ratings from scaruffi.com. Only movies from 1980 to present are listed. \nSearch is case insensitive. \n\nFor example, you can search: \nDavid Lynch \nallen \nwes Anderson \nthe great beauty \nChan-wook \n \nOr you can use commands like /best1980s, /best1970s, etc.. to retrieve the list of the best movies of a decade.\n\nDeveloper: @salvdelg. You can find the code on https://github.com/gammaray05/scarufficinema")

@bot.message_handler(commands=['alltime'])
def start(message):
    bot.reply_to(message, alltimet.text)

@bot.message_handler(commands=['best1910s'])
def start(message):
    bot.reply_to(message, diecit.text)

@bot.message_handler(commands=['best1920s'])
def start(message):
    bot.reply_to(message, ventit.text)

@bot.message_handler(commands=['best1930s'])
def start(message):
    bot.reply_to(message, trentat.text)

@bot.message_handler(commands=['best1940s'])
def start(message):
    bot.reply_to(message, quarantat.text)

@bot.message_handler(commands=['best1950s'])
def start(message):
    bot.reply_to(message, cinquantat.text)

@bot.message_handler(commands=['best1960s'])
def start(message):
    bot.reply_to(message, sessantat.text)

@bot.message_handler(commands=['best1970s'])
def start(message):
    bot.reply_to(message, settantat.text)

@bot.message_handler(commands=['best1980s'])
def start(message):
    bot.reply_to(message, ottantat.text)

@bot.message_handler(commands=['best1990s'])
def start(message):
    bot.reply_to(message, novantat.text)

@bot.message_handler(commands=['best2000s'])
def start(message):
    bot.reply_to(message, zerozerot.text)

@bot.message_handler(commands=['best2010s'])
def start(message):
    bot.reply_to(message, zerodiecit.text)

#handle searching
@bot.message_handler(func=lambda message: True, content_types=['text'])
def start(message):
    bot.reply_to(message, "Searching...")
    start_time = time.perf_counter()
    text = message.text
    reversetext = " ".join(text.split(" ")[::-1])
    result = df[df['DIRECTOR'].str.contains(text, case=False, regex=False) | df['DIRECTOR'].str.contains(reversetext, case=False, regex=False) | df['MOVIE'].str.contains(text, case=False, regex=False)]
    resultlist = result.values.T.tolist()
    zippedlist = list(zip(*resultlist))
    final = "\n".join([" - ".join(map(str, tup)) for tup in zippedlist])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    if not final:
        bot.reply_to(message, "No results found. Check the title or the name. \n\nPlease:\n* Don't search for a director and a movie together\n* Use the English title of a movie\n* Remember that only movies from 1980 to present are listed\n* Use correctly the '-' if you're searching for directors with it in the name (e.g. 'Chan-Wook', 'Joon-ho').")
    else:
        bot.reply_to(message, final + "\n\nLast updated on: " + timestamp.text + f"\n\nElapsed time: {elapsed_time:.6f} seconds")

#stay on alert
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=URL + TOKEN)
    return "!", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))