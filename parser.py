from lxml import html
import re
import requests
import csv
from csv import writer
import operator
import os
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString, Tag

#defining git pushing function
def git_push():
    try:
        os.system('cmd /c "git add ."')
        os.system('cmd /c "git commit -m "updated list""')
        os.system('cmd /c "git push -u origin master -f"')
        print("Success")
    except:
        print("Error while git automating")

#create timestamp for last updated message
now = datetime.now()
timestamp = now.strftime("%B %d, %Y")
with open("timestamp.txt", "w") as file:
    file.write(timestamp)

#urls list
urls = ['https://www.scaruffi.com/cinema/best80.html','https://www.scaruffi.com/cinema/best81.html','https://www.scaruffi.com/cinema/best82.html','https://www.scaruffi.com/cinema/best83.html','https://www.scaruffi.com/cinema/best84.html','https://www.scaruffi.com/cinema/best85.html','https://www.scaruffi.com/cinema/best86.html','https://www.scaruffi.com/cinema/best87.html','https://www.scaruffi.com/cinema/best88.html','https://www.scaruffi.com/cinema/best89.html','https://www.scaruffi.com/cinema/best90.html','https://www.scaruffi.com/cinema/best91.html','https://www.scaruffi.com/cinema/best92.html','https://www.scaruffi.com/cinema/best93.html','https://www.scaruffi.com/cinema/best94.html','https://www.scaruffi.com/cinema/best95.html','https://www.scaruffi.com/cinema/best96.html','https://www.scaruffi.com/cinema/best97.html','https://www.scaruffi.com/cinema/best98.html', 'https://www.scaruffi.com/cinema/best99.html', 'https://www.scaruffi.com/cinema/best00.html', 'https://www.scaruffi.com/cinema/best01.html', 'https://www.scaruffi.com/cinema/best02.html', 'https://www.scaruffi.com/cinema/best03.html', 'https://www.scaruffi.com/cinema/best04.html', 'https://www.scaruffi.com/cinema/best05.html', 'https://www.scaruffi.com/cinema/best06.html', 'https://www.scaruffi.com/cinema/best07.html', 'https://www.scaruffi.com/cinema/best08.html', 'https://www.scaruffi.com/cinema/best09.html', 'https://www.scaruffi.com/cinema/best10.html', 'https://www.scaruffi.com/cinema/best11.html', 'https://www.scaruffi.com/cinema/best12.html', 'https://www.scaruffi.com/cinema/best13.html','https://www.scaruffi.com/cinema/best14.html', 'https://www.scaruffi.com/cinema/best15.html', 'https://www.scaruffi.com/cinema/best16.html', 'https://www.scaruffi.com/cinema/best17.html', 'https://www.scaruffi.com/cinema/best18.html', 'https://www.scaruffi.com/cinema/best19.html', 'https://www.scaruffi.com/cinema/best20.html', 'https://www.scaruffi.com/cinema/best21.html', 'https://www.scaruffi.com/cinema/best22.html']

# csv writer function
def append_list_as_row(file_name, list_of_elem):
    headers = ["RATING","DIRECTOR","MOVIE"]
    with open(file_name, 'a+', newline='', encoding='utf8') as write_obj:
        file_is_empty = os.stat(file_name).st_size == 0
        csv_writer = writer(write_obj)
        if file_is_empty:
            csv_writer.writerow(headers)
        csv_writer.writerow(list_of_elem)

if os.path.exists("../unsortedlist.csv"):
    os.remove("../unsortedlist.csv")

# parse the urls list and search for ratings, then append to csv
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
                else:
                    append_list_as_row('../unsortedlist.csv', e)

# sort the csv by ratings
data = csv.reader(open('../unsortedlist.csv'),delimiter=',')
sortedlist = sorted(data, reverse=True, key=operator.itemgetter(0))
with open("list.csv", "w") as f:
    fileWriter = csv.writer(f, delimiter=',', lineterminator='\n')
    for row in sortedlist:
        fileWriter.writerow(row)


# update git
# git_push()