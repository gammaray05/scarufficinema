from lxml import html
import re
import requests
from csv import writer
import os
import time
from bs4 import BeautifulSoup, NavigableString, Tag


urls = ['https://www.scaruffi.com/cinema/best98.html', 'https://www.scaruffi.com/cinema/best99.html', 'https://www.scaruffi.com/cinema/best00.html', 'https://www.scaruffi.com/cinema/best01.html', 'https://www.scaruffi.com/cinema/best02.html', 'https://www.scaruffi.com/cinema/best03.html', 'https://www.scaruffi.com/cinema/best04.html', 'https://www.scaruffi.com/cinema/best05.html', 'https://www.scaruffi.com/cinema/best06.html', 'https://www.scaruffi.com/cinema/best07.html', 'https://www.scaruffi.com/cinema/best08.html', 'https://www.scaruffi.com/cinema/best09.html', 'https://www.scaruffi.com/cinema/best10.html', 'https://www.scaruffi.com/cinema/best11.html', 'https://www.scaruffi.com/cinema/best12.html', 'https://www.scaruffi.com/cinema/best13.html','https://www.scaruffi.com/cinema/best14.html', 'https://www.scaruffi.com/cinema/best15.html', 'https://www.scaruffi.com/cinema/best16.html', 'https://www.scaruffi.com/cinema/best17.html', 'https://www.scaruffi.com/cinema/best18.html', 'https://www.scaruffi.com/cinema/best19.html', 'https://www.scaruffi.com/cinema/best20.html']


def append_list_as_row(file_name, list_of_elem):
    headers = ["RATING","DIRECTOR","MOVIE"]
    with open(file_name, 'a+', newline='', encoding='utf8') as write_obj:
        file_is_empty = os.stat(file_name).st_size == 0
        csv_writer = writer(write_obj)
        if file_is_empty:
            csv_writer.writerow(headers)
        csv_writer.writerow(list_of_elem)

os.remove("c:/Users/pc/Desktop/PROGETTI/scaruffi cinema bot/list.csv")

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for a in soup.find_all('table'):
        b = (a.get_text())
        for line in b.split('\n'):
            if re.match("^[0-9].*|^\s[0-9].*|^\s\s[0-9].*" ,line):
                c = re.findall("(\d\.\d)([^:]+): (.+)", line)
                try:
                    d = list(c[0])
                    e = [e.rstrip() for e in d]
                except IndexError:
                    print("Movie with formatting error")
                append_list_as_row('c:/Users/pc/Desktop/PROGETTI/scaruffi cinema bot/list.csv', e)