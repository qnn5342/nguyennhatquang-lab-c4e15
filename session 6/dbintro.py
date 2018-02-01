
from pymongo import MongoClient

mongol_url = "mongodb://admin:admin@ds119688.mlab.com:19688/quangawesome"

#1. Open a connection to mlab
client = MongoClient(mongol_url)

#2. Get a database
db = client.get_default_database() # only 01 wardrobe

#3. Get collection
games = db['games'] # retrieve collection
blog = db['blog']

games_list = games.find ()

for game in games_list:
    print (game)
#4. Create new document
#
# new_game = {
# 'title':'Witcher 3',
# 'description': 'good game'
# }
#
# new_blog = {
# 'Day 1': 'setting goal'
# }
#
# #5. Put created document into collection
# blog.insert_one(new_blog)
