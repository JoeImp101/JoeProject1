# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:38:16 2018

@author: jimperato
"""

import sys
import os
import textwrap

def hello():
    """Print "Hello World" and return None"""
    print("Hello my name is Tommy.")

hello()

print(textwrap.fill(sys.version),'\n')

mwd = os.getcwd()
print("My working directory:\n" + mwd)

print("My CPU count is :" + str(os.cpu_count()))

print("My OS name is :" + str(os.name))

var1 = "This is a test string"


print(var1.upper())

print(var1.split())

print("iterating thru a string with a for loop:")
for i in var1:
    print(i)
print("Splitting a string into a list and then iterating with a for loop:")
for i in var1.split():
    print (i)
    
x = 3.6+4
print(type(x))    
 
print("\nForce a float:\n")  
y = float(3) + 4
print(type(y))    

print("\nBooleans:\n")
print(True or False)
print(True and False)
print(3 == 4)
print(3 != 4)
print((3 == 3) and (4==8))

print("\nTuples:\n")
tup1 = 3,4,5,6
tup2 = (3,4,5,6)
print(tup1 == tup2)

print(tup1[1])
#tup1[1] = 55

print("\nNesting of tuples:")
nest = (("the","first"),("the","second"))
print(nest[0])
print(nest[0][0])
print(nest[0][0][2])  
print(type(nest))

print("\nUnpacking of tuples:")
a,b = nest
print(a)
print(b)
(a1,a2),(b1,b2) = nest
print(a1)
('the', 'first')

print("\nRange is object of integers from builtin module:")

num=50
jrange=range(num)
print(type(jrange))
print (jrange)

print("\nCan create other types from range. Tuple here:")
trange=tuple(range(num))
print(type(trange))
print(trange)

print("\nCan create other types from range. List here:")
lrange=list(range(num))
print(type(lrange))
print(lrange)


print("\nCall previously defined hello function:")
hello()

joedict = {'Dad': 80, 'Mom': 78, 'Joe': 39, 'Chris': 36}

print("\nDictionaries:")

print(type(joedict))
print (joedict['Chris'])
print(joedict.keys())
print(joedict.values())
print(joedict.get('Mom'))

print("\nDictionary Loop:")
for i in joedict:
    print (i, 'is', joedict[i], 'years old. ')

joedict.update({'Tom':10})

print("\nDictionary Loop after additional item added:")
for i in joedict:
    print (i, 'is', joedict[i], 'years old. ')

dic1={1:10, 2:20} 
dic3={3:30, 4:40} 
dic2={5:50,6:60}
dictotal= {}

print("\nConcatenating multiple dictionaries into 1:")
print ("Dic1 = ", dic1)
print ("Dic2 = ", dic2)
print ("Dic3 = ", dic3)

for i in (dic1, dic2, dic3): 
    dictotal.update(i)

print ("DicTotal = ", dictotal)

print ("Sorted DicTotal (returns List not Dictionary) = ", sorted(dictotal))

print ("\nUnsorted DicTotal iteration:")
for i in dictotal:
    print (i, 'is', dictotal[i], 'years old. ')

print ("\nSorted DicTotal iteration:")
for i in sorted(dictotal):
    print ( i, 'is', dictotal[i], 'years old. ')
    
print ("\nFind particular key in dictionary:")
for i in dictotal:
    if   i == 4:
        print ("Found #4 key")
    elif i == 17:
        print ("Found #17 key")
    else:       
        print ("Wasn't looking for key", i)

print ("\nFind particular value in dictionary:")
for i in dictotal:
    if   dictotal[i] == 40:
        print ("Found 40 value")
    elif dictotal[i] == 17:
        print ("Found 17 value")
    else:       
        print ("Wasn't looking for value", dictotal[i])


#Exercise #7 from 
#https://www.w3resource.com/python-exercises/dictionary/        
print ("\nGenerate dictionary that is x, x*x: ")

n=50
square_dict = {}
work_dict = {}
i=1    
while i<=n+1 :
    work_dict = {i:i*i}
    print("work_dict = ", work_dict)
    square_dict.update(work_dict)
    i=i+1

print ("\nThe created dictionary of up to n is: \n", square_dict)

print ("\nAnother way to generate dictionary that is x, x*x: ")

square_dict2 = dict() #builtin function that creates dict from scratch

for n in range(1,n+1):
    square_dict2[n] = n*n
    
print ("\nThe created dictionary of squares the better way is: \n", square_dict2)

#Exercise #10 from 
#https://www.w3resource.com/python-exercises/dictionary/        
print ("\nSum of all the items in a dictionary: ")

print ("\nIn this dictionary: \n", square_dict2)

dict_sum = 0
for n in range(1,n+1):
    dict_sum = dict_sum + square_dict2[n]

    
print ("\nThe sum of all the values is: \n", dict_sum)

#Exercise #13 from 
#https://www.w3resource.com/python-exercises/dictionary/  
      
print ("\nMap 2 lists into a dictionary: ")    
#You can use the zip function to iterate through any 2 iterable objects to merge them
#into a zip object , which can then be converted into whatever you want , either a
#list, tuple, or dictionary
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_zip = zip(keys, values)
color_dictionary = dict(color_zip)
print(color_zip)
print(color_dictionary)   

ziprange = tuple(zip( range(5), range(1,20,2) ))
print(type(ziprange))
print(ziprange)
ziprange = list(ziprange)
print(type(ziprange))
print(ziprange)
ziprange = dict(ziprange)
print(type(ziprange))
print(ziprange)

#List  Comprehension
#Create lists using concise for loops
print("\nList Comprehension :")
x1 = range(10)
y1 = []
for i in x1:
    y1.append(i*i)
print('x1 list:',x1)
print('y1 list:',y1)
x1list = [i*i for i in range(10)]
print (x1list)

print([i*i if i > 0 else i for i in range(-5,5)])

print ("\nLambda functions :")
lam_func2 = lambda x1,x2: (x1 + x2,x1 - x2)
print(lam_func2(3,4))
