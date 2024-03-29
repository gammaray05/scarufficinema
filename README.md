# Scaruffi's Cinema Ratings Parser and Telegram Bot
### What is this

A weekly updated and data miners-friendly list of movie ratings by Piero Scaruffi ([scaruffi.com](https://scaruffi.com)), from 1980 to present *(why 1980? Because it is the first year that Piero have movie ratings for every year with numbers and not just with simple rankings)*. In the "best by decades" folder there are the best by decade lists parsed manually.
Ratings are parsed in parser.py.
Columns are ratings, directors and movies (for now).


### Telegram Bot @scaruffi_cinemabot

In main.py you can find a simple Telegram bot made using pyTelegramBotAPI library, Flask and Pandas, that search inside the CSV and return an easy-to-read list of ratings. You can find it on telegram on [@scaruffi_cinemabot](https://t.me/scaruffi_cinemabot).
Start the bot, then you can type a movie (using the English title) or a director
and you will obtain the search results with ratings. Or you can use commands like */best1970s*, */best1980s*, etc.. to retrieve the best by decade lists.

### What to do next

* Parsing movies metadata, especially for showing movie years in search results. 
* Show other ratings, like Metascore or IMDB, for comparison.
