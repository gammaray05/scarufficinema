# Scaruffi Cinema Ratings CSV List and Telegram Bot
## What is this

A time-to-time updated and data miners-friendly list of movie ratings by Piero Scaruffi ([scaruffi.com](scaruffi.com)), from 1998 to present *(why 1998? Because it is the first year that Piero posted movie ratings for every year with numbers and not just with simple rankings)*.
Parsed by parser.py. 
Columns are ratings, directors and movies (for now).


**Telegram Bot @scaruffi_cinemabot**

In WebhookBot.py you can find a simple Telegram bot made using Telepot library and Pandas, that search inside the CSV and return an easy-to-read list of ratings. Or you can retrieve lists of the best movies of a decade by using commands. You can find it on telegram on [@scaruffi_cinemabot](https://t.me/scaruffi_cinemabot).
Start the bot, then you can type a movie (using the English title) or a director
and you will obtain the search results with ratings.

Deployed to PythonAnywhere *(very nice free service that requires one login every 3 months to mantain the bot running, much better than the 30 minutes timeout and complexities of Heroku)*.

**What to do next**

* Parsing movies metadata, especially for showing movie years in search results. 
* Show other ratings, like Metascore or IMDB.
