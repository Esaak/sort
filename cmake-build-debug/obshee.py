from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12, 7))
with open('sort_bubble.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y = [float(item[0]) for item in data]
x = [float(item[1]) for item in data]
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
#plt.scatter(x,m*x+c)
line1, = plt.loglog(x,y, color='g', label= 'sort_bubble')
with open('sort_insertion.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y1= [float(item[0]) for item in data]
x1= [float(item[1]) for item in data]
line2, =plt.loglog(x1,y1, color ='r', label= 'sort_insertion')
with open('sort_selection.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y2= [float(item[0]) for item in data]
x2= [float(item[1]) for item in data]
line3, = plt.loglog(x2,y2, color ='b', label='sort_selection')


plt.grid()
plt.legend(( line3, line2, line1), ['sort_selection','sort_insertion', 'sort_bubble'])
plt.show()
