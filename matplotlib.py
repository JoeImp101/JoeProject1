# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:04:12 2018

@author: jimperato
"""
from matplotlib import pyplot as plt

x = range(-5,5)
y = [i**3 for i in x]

print (type(x))
print (type(y))

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()