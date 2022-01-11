from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12, 7))
with open('O0_sort_insertion.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y = [float(item[0]) for item in data]
x = [float(item[1]) for item in data]

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
#plt.scatter(x,m*x+c)
line1, = plt.plot(x,y, color='g', label= 'sort_bubble')
with open('OO0_sort_insertion.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y1= [float(item[0]) for item in data]
x1= [float(item[1]) for item in data]
line2, =plt.plot(x1,y1, color ='r', label= 'sort_insertion')
with open('2_sort_bubble.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y2= [float(item[0]) for item in data]
x2= [float(item[1]) for item in data]
line3, = plt.plot(x2,y2, color ='b', label='sort_insertion')

plt.grid()
plt.legend((line3,line2,  line1), ['sort_insertion_average','sort_insertion_best', 'sort_insertion_bad'])
#plt.legend((line8, line7, line6), ['sort_insertion','sort_quick', 'sort_quick'])
plt.show()