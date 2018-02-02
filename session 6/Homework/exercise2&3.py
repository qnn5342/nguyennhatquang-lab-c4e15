import win_unicode_console
win_unicode_console.enable()

from pymongo import MongoClient

mongol_url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Open a connection to mlab
client = MongoClient(mongol_url)

db = client.get_default_database() # only 01 wardrobe

#3. Get collection
post= db['posts']

allpost = post.find()

# for post in allpost:
#     print(post)

#Write  new posts

new_post = {
'title': 'Cảm nghĩ của Quang',
'author': 'Nguyen Nhat Quang',
'content': '''I am here doing homework for lab1. My previous code did not run and i don't know why
 i hope this code runs and i know why.

 '''

}

insert_one

post.insert_one(new_post)
