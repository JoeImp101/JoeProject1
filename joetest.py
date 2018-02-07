#-----Python list example-----
#-----lISTS HAVE [].
#-----TUPLES HAVE ()
#-----DICTIONARIES HAVE {}
family=['mom', 'daddy' , 'bro' ,'sis' ,'dog']
print((family[3])) # starts from zero
print((family[-1])) # -1 is the last elforement in the list

x='joe'
print('joe'[2]) # can access chars in a string by list notation

#------Slicing Lists---

example=[0,1,2,3,4,5,6,7,8,9]
print(example[2:6])
print(example [-5:]) # start from left go 5 back to 5 and select all up to the end
print(example)
print(example [1:8:2]) # start at 1, go until 8, count by 2s
print(example [::-2]) # include everything and count backward by 2

#-------Editing Lists------
print([7,4,5] + [4,6,5]) # concatenate list
print('joe' + 'shmo') # concat string
print('joe'*10) #repeats 10 times
print(21*10) # returns the math 210
print([21]*10) # 21 is now an element in a list and its repeated 10 times

name='test'
print("variable \'name\' set to \'test\'. Is letter z in \'test\'? " , 'z' in name)  # returns true or false
print("how bout \'t\'", 't' in name)  # returns true
print("Is dad in family list? ", 'dad' in family)

print("Length of family list is: ", len (family)) # returns # of elements

numbers= [8,1,4,17,28,165,7]
print(numbers)
numbers[3] = 77 # changed 3rd element
print(numbers)
del numbers[3] # removes element
print(numbers)
print(list('bucky')) # converts string to list

#----more list manipulation----
example=list('easyhoss')
print(example)
example[4:]=list('baby') # replaces elements starting at 4 with string chars 
print(example)

#-----methods----
sentencelist = ['i', 'love', 'apples', 'apples', 'now']
print("occurences of apples in sentencelist: ", sentencelist.count('apples'))

#-------------indexes----

say=['hey', 'now' , 'brown', 'cow']
print(say)
print(say.index('brown'))
say.insert(2,'hoss')
print(say)
say.pop(1)
print(say)
say.remove('cow')
print(say)
say.reverse()
print(say)

#-------------tuples-----
#very static. Just used for permanent lists
# cant change them

joe=(1,2,3,4)
print("tuple joe = ", joe)
print(joe[3])


#-----string manip-------
bigstring = "hey there %s, hows your %s"
varb=('betty', 'foot')
print(bigstring % varb)

joestring='hello there bob'
print(joestring.find('bob'))

#------------Dictionary----
book = {'Dad':'Bob', 'Mom':'Lisa', 'Bro':'Joe'}
print(book)
print(book['Dad'])
#book.clear()
print(book)

tuna = book.copy()

print(tuna, book)

print('Mom' in tuna)
print('dude' in tuna)

#------------IF stmts-------------
fish="bass"
print("Fish = ", fish)
if fish=="tuna":
    print("yes the fish is a tuna")
elif fish=="salmon":
    print("fish is a salmon")
elif fish=="bass":
    print("fish is a bass")
else:
    print("Not sure which fish it is.")


#----nested ifs--------

thing= "animal"
animal = "toad"

print("thing is %s " % thing , "animal is %s" % animal)

if thing=="animal":
    if animal=="cat":
        print("Its an animal and a cat")
    else:
        print("Dont know what animal it is")
else:
    print("i dont know what this thing is")


#----other comparison operators
print(9<7)
print(9<=9)
print(9!=3)
print(9!=9)

#-----is operator---
one = [1,2,3]
two = [1,2,3]
print(one,two)
print(one == two)  # prints true because both lists are equivalent
print(one is two) # prints false because they are not the SAME OBJECT

three = four = [3,4,5]
print(three,four)
print("is three same as four?", three is four) # prints true because three is same object as four

#-----in operator----
pizza="pizzahut"
print("pizza variable= ", pizza)
print("Is h in pizza?", "h" in pizza) # true
print("Is x in pizza?", "x" in pizza) # false

#----and operator (same for or)
example=2
print("example is ", example)
if example > 3 and example < 10:
    print("example is between 3 and 10")
else:
    print("example is not between 3 and 10")

#------while loops-----

b=1
while b <=10:
    print(b)
    b+=1

#------for loops----
gl=['bread', 'milk', 'meat','beef']
print(gl)

for food in gl:
    print(food)

#----looping thru a dictionary---
ages={'dad':45, 'mom':49, 'katey':10, 'tommy':8}
print(ages)
for item in ages:
    print(item + " is " + str(ages[item]) + " years old.")

#---infinite while loop. Create a list from input-----
namelist = []
while 1:  # always true so goes on forever
 #   name = input('Enter name: ')
    name='quit'  #delete this line to perform this test
    if name == 'quit':
        print(namelist)
        break
    else:
        namelist.append(name)
        print("The namelist list is currently: ", namelist)
    
def press_to_continue():
    while 1:  # always true so goes on forever
           quit = input('Press any key and Enter to continue...')
           if quit: 
               break

#-----functions----

def whatsup(x):
    return 'whats up ' + x

print(whatsup('joe'))

y=5

def plusten(y):
    return y+10

print("y is ", y , "y + 10 is ", plusten(y))

def func(first='tom',last='smith'):
    print('%s  %s' % (first,last))

print(func('bill', 'ted'))
print(func())
print(func('joe'))
print(func(last='roberts'))

#---convert params to tuples in fucntions
def newlist(*food):    # the asterisk allows variable amt of params which are loaded into a tuple
    return food

food=newlist('apples', 'carrots', 'beef', 'chicken', 'beets')

print("Newlist tuple = ", food)

press_to_continue()

for items in food:
    print ("Newlist item #", items  , "is: ", food(items))

press_to_continue()


print(newlist('tacos', 'pizza'))

def profile(name, *ages): # multiple params where 1 param is a tuple
    return name , ages

print(profile('bucky', 42,43,44,45))

#----convert params to dictionary----
def cart(**items):
    return items

print(cart(apples=4, peaches=6, beef=60))

def profile2(name, *ages, **items): # multiple params where 1 param is a tuple
    return name , ages, items


print(profile2('bucky', 42,43,44,45, bacon=4, eggs=2, toast=5))

#----pass a tuple to a function-------
def tupleexample (a,b,c):
    return a+b+c

tunatuple = (5,7,3)
print("tupleexample returns : ", tupleexample(*tunatuple))

#----pass a dictionary to a function
def example2(**this):
    return this

bacon={'momma':32, 'dad':34}

print(example2(**bacon))

#-----OO and classes---

class exampleClass:
    eyes="blue"
    age=22

    def thismethod(self):   # always need self
        return 'hey this method worked'

exampleObject=exampleClass()

print(exampleObject.eyes, exampleObject.age, exampleObject.thisMethod())

#------use of self in classes. "self" is needed because it contains the name of the object that you instantiated
class className:
    def createName(self, name):
        self.name=name
    def displayName(self):
        print(self.name)
    def saying(self):
        print("hello %s" % self.name)

first=className()
second=className()
first.createName('bucky')
second.createName('tony')
first.displayName()
first.saying()
second.displayName()
second.saying()

#-----Subclasses and Superclasses
class parentClass:
    var1="i am var1"
    var2="i am var2"

class childClass(parentClass): # inherits properties of parentClass
    pass        #dont do anything

parentObject=parentClass()
print(parentObject.var1)

childObject=childClass()
print(childObject.var1, childObject.var2) #this works because it has inherited from parentClass

class childClass2(parentClass):
        var2="i am the overwritten var2"

cob2=childClass2()
print(cob2.var1, cob2.var2)

#-----Multiple Parent Classes inheritance
class Mom:
    var1= "i am Mom"

class Dad:
    var2="i am dad"

class Child(Mom,Dad):
    var3="im the childvar"

cobj= Child()

print(cobj.var1, cobj.var2, cobj.var3)


#------------Constructors-------

class Swine:
    def __init__(self): # this initializes the class and performs whatever is within upon instantiation of the class
        print("I was part of __init__ method")

obj=Swine()  # when you run this line of code it prints beef pie without haveing to do anything

#----Modules----

import joemodule #created a file in path called joemodule.py
import imp

print(joemodule.testmodule())

baby=joemodule.testmodule #assign the module to a variable as a shorcut

print("the baby module rename is ", baby())   # then you can call it like this

print(imp.reload(joemodule)) # allows you to reload a module if changed

#------more modules---

print(dir(joemodule))  # lists the contents of a module

help(joemodule) # lists details of each  part of a module

print("------------")

print(joemodule.__doc__) # gives a quick summary of the module. joemodule doesnt have one.

import math
print("Math module doc is:")
print(math.__doc__) # but math does

#-----working with files----

fileobject=open('c:/python27/a.txt' ,'a')
#fileobject.write('hey now brown cow') # comment out so it doesnt keep writing every time
fileobject.close()

fileobject=open('c:/python27/a.txt' ,'r')
#print fileobject.read(3) # reads first 3 chars which is 'hey'
#print fileobject.readline()
print(fileobject.readlines()) # reads the whole file line by line and stores in list
fileobject.close()



