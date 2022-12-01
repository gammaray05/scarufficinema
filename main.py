from flask import Flask, request
import requests
import telebot
import pandas as pd
import os

#initialize resources
url="https://raw.githubusercontent.com/gammaray05/scarufficinema/master/list.csv"
tsurl = "https://raw.githubusercontent.com/gammaray05/scarufficinema/master/timestamp.txt"
timestamp = requests.get(tsurl)
master = pd.read_csv(url, sep=',', names = ['RATING', 'DIRECTOR', 'MOVIE'])

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
@bot.message_handler(commands=['start', 'alltime', 'best1910s', 'best1920s', 'best1930s', 'best1940s', 'best1950s', 'best1960s', 'best1970s', 'best1980s', 'best1990s', 'best2000s', 'best2010s'])
def handle_command(message):
    command = message.text.split()[0][1:]  # Get the command from the message

    if command == 'start':
        bot.reply_to(message, "Please, type a movie (English title) OR a director to search ratings from scaruffi.com. Only movies from 1980 to present are listed. \nSearch is case insensitive. \n\nFor example, you can search: \nDavid Lynch \nallen \nwes Anderson \nthe great beauty \nChan-wook \n \nOr you can use commands like /best1980s, /best1970s, etc.. to retrieve the list of the best movies of a decade.\n\nDeveloper: @salvdelg. You can find the code on https://github.com/gammaray05/scarufficinema")

    elif command == 'alltime':
        bot.reply_to(message, alltimet.text)
    elif command == 'best1910s':
        bot.reply_to(message, diecit.text)
    elif command == 'best1920s':
        bot.reply_to(message, ventit.text)
    elif command == 'best1930s':
        bot.reply_to(message, trentat.text)
    elif command == 'best1940s':
        bot.reply_to(message, quarantat.text)
    elif command == 'best1950s':
        bot.reply_to(message, cinquantat.text)
    elif command == 'best1960s':
        bot.reply_to(message, sessantat.text)
    elif command == 'best1970s':
        bot.reply_to(message, settantat.text)
    elif command == 'best1980s':
        bot.reply_to(message, ottantat.text)
    elif command == 'best1990s':
        bot.reply_to(message, novantat.text)
    elif command == 'best2000s':
        bot.reply_to(message, zerozerot.text)
    elif command == 'best2010s':
        bot.reply_to(message, zerodiecit.text)

#handle searching
@bot.message_handler(func=lambda message: True, content_types=['text'])
def start(message):
    bot.reply_to(message, "Searching...")
    text = message.text
    reversetext = " ".join(text.split(" ")[::-1])

# Select rows that match the search criteria
    result = master.loc[
    (master['DIRECTOR'].str.contains(text, case=False, regex=False)) | 
    (master['DIRECTOR'].str.contains(reversetext, case=False, regex=False)) | 
    (master['MOVIE'].str.contains(text, case=False, regex=False))
]
    result = result[['DIRECTOR', 'MOVIE']]
    final = "\n".join([" - ".join(tup) for tup in result.values])

    if not final:
        bot.reply_to(message, "No results found. Check the title or the name. \n\nPlease:\n* Don't search for a director and a movie together\n* Use the English title of a movie\n* Remember that only movies from 1980 to present are listed\n* Use correctly the '-' if you're searching for directors with it in the name (e.g. 'Chan-Wook', 'Joon-ho').")
    else:
        bot.reply_to(message, final + "\n\nLast updated on: " + timestamp.text)

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