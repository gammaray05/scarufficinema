import os
import pandas as pd
import sys
import time
import telepot
from telepot.loop import MessageLoop


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        
        if msg['text'] == "/start":
            bot.sendMessage(chat_id, "Please, type a movie (English title) or a director to search ratings from scaruffi.com")
            return
        
        search = msg['text']
        url="https://raw.githubusercontent.com/gammaray05/scarufficinema/master/list.csv"
        master = pd.read_csv(url, sep=';', names = ['RATING', 'DIRECTOR', 'MOVIE'])
        result = master[ master['DIRECTOR'].str.contains(search, case=False, regex=False) | master['MOVIE'].str.contains(search, case=False, regex=False) ]
        resultlist = result.values.T.tolist()
        zippedlist = list(zip(*resultlist))
        final = "\n".join([" - ".join(tup) for tup in zippedlist])
        if not final:
            bot.sendMessage(chat_id, "No results found. Check the title or the name and please remember to use the English title of the movie.")
        else: 
            bot.sendMessage(chat_id, final)
     
TOKEN ='token'        
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)
