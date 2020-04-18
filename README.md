# Scaruffi Cinema Ratings 
## What is that

A time-to-time updated and data miners-friendly list of movie ratings by Piero Scaruffi (scaruffi.com), from 1998 to present (why 1998? Because it is the first year that Piero posted movie ratings for every year with numbers and not just with simple rankings).
Parsed by parser.py. 
Columns are ratings, directors and movies (for now).


**Telegram Bot @scaruffi_cinemabot**

In WebhookBot.py you can find a simple Telegram bot made using Telepot library and Pandas, that search inside the CSV and return an easy-to-read list of ratings. Or you can retrieve lists of the best movies of a decade by using commands. You can find it on telegram on [@scaruffi_cinemabot](https://t.me/scaruffi_cinemabot).
Deployed to PythonAnywhere (very nice free service that requires one login every 3 months to mantain the bot running, *much better than the 30 minutes timeout and complexities of Heroku*).
There is also the "standard" version of the Bot that does not rely on Webhook Telegram API and Flask to run.

**What to do next**

If someone can help me parsing movies metadata that would be great: years of the movies above all, but it would be fun to compare with Metascore's ratings also.
