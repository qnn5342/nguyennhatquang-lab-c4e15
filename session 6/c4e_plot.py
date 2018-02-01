from matplotlib import pyplot
#1. Prepare database
label = ['ios', 'android', 'web']
values = [3033,4000,5803]
colors = ['red', 'blue', 'grey']
explode = [0, 0.2, 0]

#2. Plot
pyplot.pie(values, labels = label, colors =colors, explode= explode)

pyplot.axis('equal')

#3. Show
pyplot.show()
