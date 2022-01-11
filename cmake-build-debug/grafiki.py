from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(12, 7))
with open('O01_sort_heap.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y = [float(item[0]) for item in data]
x = [float(item[1]) for item in data]
x= np.array(x)
y=np.array(y)

x11=np.copy(x*np.log(x))
y=y/x11
line1, = plt.plot(x,y, color='g', alpha = 0.3)
xxyy = np.polyfit(x,y,1)
#yy0 = np.polyval(x,xxyy)
yy0=x*xxyy[0]+xxyy[1]
line4, = plt.plot(x,yy0, color = 'g', alpha =1)
with open('O01_sort_quick.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y2= [float(item[0]) for item in data]
x2= [float(item[1]) for item in data]
x2= np.array(x2)
y2=np.array(y2)
x21=np.copy(x2*np.log(x2))
y2=y2/x21
xxyy2 = np.polyfit(x2,y2,1)
#yy0 = np.polyval(x,xxyy)
yy02=x*xxyy2[0]+xxyy2[1]
line2, = plt.plot(x2,y2, color ='b', alpha = 1)
line5, = plt.plot(x2,yy02, color ='b', alpha = 1)
with open('O01_sort_merge.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y3= [float(item[0]) for item in data]
x3= [float(item[1]) for item in data]
x3= np.array(x3)
y3=np.array(y3)
x4=np.copy(x3*np.log(x3))
y3=y3/x4
xxyy3 = np.polyfit(x3,y3,1)
#yy0 = np.polyval(x,xxyy)
yy03=x*xxyy3[0]+xxyy3[1]
line6, = plt.plot(x3,yy03, color ='y', alpha = 1)
line3, = plt.plot(x3,y3, color ='y', alpha = 0.3)
#print(x)
#print(x11)
plt.grid()
plt.legend((line6, line5, line4, line3,line2,  line1), ['merge_trend','quick_trend','heap_trend','sort_merge','sort_quick', 'sort_heap'])
plt.show()
