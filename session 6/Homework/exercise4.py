import win_unicode_console
win_unicode_console.enable()

from pymongo import MongoClient

mongol_url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Open a connection to mlab
client = MongoClient(mongol_url)

db = client.get_default_database() # only 01 wardrobe
customers= db['customers']
allclients = customers.find()

refcount ={}

for customer in allclients:
    refcount[customer['ref']] =  refcount.get(customer['ref'],0) + 1

from matplotlib import pyplot

label = []
values = []
colors = ['red', 'blue', 'yellow']
explode = [0, 0, 0]

for key, value in refcount.items():
    label.append(key)
    values.append(value)


#2. Plot
pyplot.pie(values, labels = label, colors =colors, explode= explode, autopct='%.2f%%')

pyplot.axis('equal')

#3. Show
pyplot.show()
