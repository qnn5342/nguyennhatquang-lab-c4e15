import win_unicode_console
win_unicode_console.enable()

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
output_file = "reportingnumber.xlsx"

#Part 1: scraping financial data


from urllib.request import urlopen
from bs4 import BeautifulSoup

#1. Download files

html_content = urlopen(url).read().decode('utf-8')
data = urlopen(url).read()
html_file = open("cafef.html",'wb') #write
html_file.write(data)
html_file.close()
# #2. Extract ROI
#Create a Soup
soup = BeautifulSoup(html_content, 'html.parser') # searching through xml
table = soup.find('table',id = 'tableContent') # find in table the attribute of "tablenew"
# print(table.prettify())
#  ## soup can be prettyfys
td_list = table.find_all('td')
# print data with no empty tag
data_list = []
for index, value  in enumerate(td_list):
    number = value.string
    data= {
            'Field': number
    }
    if number is not None:
        data_list.append(data)
# print (data_list)
#print data in table format
nicedatalist = []
title = ""
quarter1= ""
quarter2= ""
quarter3= ""
quarter4= ""
for index, dictionary  in enumerate(data_list):
    if index % 5 == 0:
        title = dictionary['Field']
    elif index % 5 == 1:
        quarter1 = dictionary['Field']
    elif index % 5 ==2:
        quarter2 = dictionary['Field']
    elif index % 5 ==3:
        quarter3 = dictionary['Field']
    else:
        quarter4 = dictionary['Field']
        nicedata ={
        'Name': title,
        'Quarter1': quarter1,
        "Quarter2": quarter2,
        'Quarter3': quarter3,
        'Quarter4': quarter4,
        }
        nicedatalist.append(nicedata)
print(nicedatalist)
# #3. Extract news
#install pyexcel
import pyexcel

pyexcel.save_as(records= nicedatalist, dest_file_name= output_file)
