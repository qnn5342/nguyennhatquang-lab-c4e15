import win_unicode_console
win_unicode_console.enable()

url = 'https://www.apple.com/itunes/charts/songs'
output_file = "topItunesong.xlsx"

#Part 1: scraping iTune songs


from urllib.request import urlopen
from bs4 import BeautifulSoup
#1. Download files
# #1.1 Open a connection
# conn = urlopen(url)
# #1.2 read
# data= conn.read()
# #1.3 decode
# html_content = data.decode("utf-8")
# print (html_content)

#short hand solution
html_content = urlopen(url).read()
data = urlopen(url).read()
html_file = open("iTune.html",'wb') #write
html_file.write(data)
html_file.close()
#
# #2. Extract ROI
# Create a Soup
soup = BeautifulSoup(html_content, 'html.parser') # searching through xml
ul = soup.find('ul',"") # find in ul the attribute of "ulnew"
# print(ul.prettify())
#  ## soup can be prettyfys
li_list = ul.find_all('li')
# li_list = list
songs_list = []
for li in li_list:
    h3a = li.h3.a
    h4a = li.h4.a

    song_name = h3a.string
    artists = h4a.string
    songs= {
        'Name': song_name,
        'artists': artists
        }
    # print(news_list)
    songs_list.append(songs)

#3. Extract news
## import pyexcel

# pyexcel.save_as(records= songs_list, dest_file_name= output_file)

##Now is the YouTube Part
from youtube_dl import YoutubeDL
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)

download_list = []
# print(news_list)
for dictionary in songs_list: # putting all link in a list
    download_list.append(dictionary['Name'])

# print (download_list)

for i in download_list: #loading each link at once
    dl.download(i)
