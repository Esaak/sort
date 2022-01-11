import numpy as np
import math as m
import matplotlib.pyplot    as plt
with open ('D:\informatika\sortirovka_30_10\cmake-build-debug\O0_sort_quick.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()

y= [float(item[0]) for item in data]
x = [float(item[1]) for item in data]
x= np.array(x)
y=np.array(y)
#t=0
x=x*np.log(x)
y=y/x
#t=0
#for i in x:
#    y[t]=y/(i*m.log(i))
#    t+=1
line1, = plt.plot(x,y, color='g', label= 'sort_bubble')
with open ('D:\informatika\sortirovka_30_10\cmake-build-debug\O0_sort_merge.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y1 = [float(item[0]) for item in data]
x1 = [float(item[1]) for item in data]
x1= np.array(x1)
y1=np.array(y1)
#t=0
x1=x1*np.log(x1)
y1=y1/x1
#for i in x1:
 #   y1[t]=y1/(i*m.log(i))
  #  t+=1
line2, = plt.plot(x1,y1, color='r', label= 'sort_bubble')
with open ('D:\informatika\sortirovka_30_10\cmake-build-debug\O0_sort_heap.txt') as file:
    data = file.read().split('\n')
data = [x.split('; ') for x in data if x.find('; ') != -1]
file.close()
y2 = [float(item[0]) for item in data]
x2 = [float(item[1]) for item in data]
x2= np.array(x2)
y2=np.array(y2)
#t=0
x2=x2*np.log(x2)
y2=y2/x2
line3, = plt.plot(x2,y2, color='b', label= 'sort_bubble')
plt.grid()
plt.legend((line3, line2, line1), ['sort_heap','sort_merge', 'sort_quick'])
plt.show()