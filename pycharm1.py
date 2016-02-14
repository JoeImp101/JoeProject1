# Build the steps from the Tower sample test
steplist = []
stepmax = 10
for i in range(0,stepmax):
        steplist.append(i*"#")
        #steplist[i]=i*" " +  steplist[i]
        print (steplist[i])

print (steplist)

# Print out numbers from 1 to 100 that are divisible by 4
for i in range(101):
    if i%4 is 0:   # mod statement = 0 when divisible
        print (i, "is divisible by 4")


def euros_to_usd(euros):
    dollars = euros*1.08
    print (euros, " Euros is ", dollars, " dollars.")


euros_to_usd(2)

def FtoC(Fahrenheit):
    Celsius = (5/9) * (Fahrenheit - 32)
    print (Fahrenheit, "degrees fahrenheit is ", Celsius.__round__(2), "degrees celsuis.")

FtoC (100)

def get_gender (sex="unknown"):
    if sex == "M":
        return "Male"
    elif sex == "F":
        return "Female"
    elif sex == "unknown":
        return sex

print (get_gender ('M'))
print (get_gender ('F'))
print (get_gender ("JOE"))
print (get_gender ())

# Flexible number of arguments



def add_numbers (*args):
    total = 0
    for z in args:
        total += z
    print("Add_numbers total is : ", total)
    print(args)
    print(args[3])
#numbers = [1,2,3,4,5,6,7,8,9]
#add_numbers(numbers)
add_numbers (1,2,3,4,5,6,7,8,9)


# ----------Unpacking arguments.  Pass a list to a function by using *
def health_calculator(age, apples_eaten, cigarettes):
    answer = (100-age) + (apples_eaten*3) - (cigarettes *4)
    print ("Health factor = ", answer)

print ("where am i ")
health_calculator(30, 5, 30)
joe_list= [20,50,30]
health_calculator(*joe_list)

# ------------Sets----Remove dupe values and also sort automatically

num_list = {9,8,7,6,5,22,44,66,77,3,1,1,2,3,4,5,5,6,6,7,8,9}

print("Num list set is ", num_list)

# ------------Looping thru a dictionary----

classmates = {'Joe': 'is cool', 'Mike': 'is tall', 'John': 'is nice'}

for k,v in classmates.items():
    print (k,v)

# ----- modules-------

import testmodule
import random
import math

testmodule.tuna()

x = random.randrange(1,20)

for i in range(0, x):
    print("The random number is ", x, "and we're doing it ", i+1 , "times")

# ----To add modules from the internet - Settings, Project, Project Interpreter

print ("Square root of 81 is :", math.sqrt(81))

# ------------open read write to a file --------------

fw = open('sample.txt', 'w')
fw.write("hello\n")
fw.write("how are you.\n")
fw.close()

fr = open('sample.txt')
fr_text = fr.read()
fr_text = fr.readline()

fr.close()

print(fr_text)

# -----------------download a stock price history file from yahoo----------
# -----see yahoo_stock.py

# ------------------Exception handling

while True:
    try:
        #number = int(input("What's your fav number hoss?\n"))
        number = 2
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    # except ZeroDivisionError:
    #    print("Don't pick zero")
    except:
        print("There was some kind of problem.\n")
        #break
    finally:
        print("loop complete")


# -----------------More Classes--------

class Tuna:
    def __init__(self, name):    # __init__ always runs on object creation
        self.name = name
        print (self.name, "Im a new tuna.\n")

    def swim(self):
        print (self.name, "I can swim. \n")

# -----create single instances of tuna----
tuna1 = Tuna("Mike the Tuna")
tuna2 = Tuna("Bobby the Tuna")
tuna1.swim()

# ----create an empty list of tuna objects
tuna_list = []

# ----assign 10 tuna objects to the tuna list
for i in range(1,10):
    tuna_list.append(Tuna("Tuna" + str(i)))

# ----print the name of each Tuna object in the tuna list
for i in range(0,9):
    print (tuna_list[i].name)

# --- call the swim method in each Tuna object in the tuna list
for i in range(0,9):
    tuna_list[i].swim()

# --------Class variables versus instance variables----

class Girl:

    gender = 'female'  # this is a class variable - always the same for all instances of the class

    def __init__(self, name):  # this is an instance variable. unique for every object of the class
        self.name = name

r = Girl('Rachel')
s = Girl('Stanky')
print(r.name, "is always a ", r.gender)
print(s.name , "is always a ", s.gender)

r.gender = "male"

print ("Although", r.name, "had a sex change: ", r.gender)


# --------------Inheritance-------

class Parent:

    def print_last_name(self):
        print('Roberts')


class Child(Parent):   # child class will inherit Parents attributes

    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):  # and you can override the superclass's attributes if you want
        print('Snitzleberg')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

joe = Parent()
#oe.print_first_name()    # this will not work as parent class has no first name method


# --------Multiple Inheritance----

class Mario():
    def move(self):
        print('I am moving!')

class Shroom():
    def eat_shroom(self):
        print('Now I am big!')

class BigMario(Mario, Shroom):   # Big Mario inherits from 2 classes
    pass       # the do nothing statement

bm = BigMario()
bm.move()
bm.eat_shroom()


# --------------------Threading-------

import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(5):   #underscore here is python dummychar that lets you run a for loop without a variable
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Sent out messages')
y = BuckysMessenger(name='Received messages')
x.start()   # the start method of the Threading class always looks for a run function
y.start()   # x.start starts to run and then y.start starts to run even though x.start hasnt finished.

# thus the jumbled prints

# -------------unpacking list elements into variables

def drop_first_last(grades):

    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print("first was", first, "avg is ", avg, "last was ", last)
    print("middle is ", middle)

print ("where am i")
drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])

# -----------------The zip function-----------

first = ['Bucky', 'Tom', 'Taylor', 'Bob', 'Mike', 'Pepe']
last = ['Roberts', 'Hanks', 'Swift', 'Jones', 'Hunt', 'Roni', 'Smith', 'Czervik']

names = zip(first, last)

# see Below...the next method returns a tuple of the ith element from
# each list that was zipped. until it reaches
# the one that has no more element to pair with , then
# raises the stop iteration exception
# which is why u dont see smith and czervik returned
# in this example
while 1==1:
    try:
        print (names.__next__())
    except:
        StopIteration
        break


# ----------The lambda function

answer = lambda x: x*7    #  create a simple quick function

print ("the lambda function returns ", answer(5))

# -------------------------------------

student_scores = {'Adama': 100, 'Starbuck': 75, 'Apollo': 80, 'Athena': 85, 'Agathon': 90}

all_scores = student_scores.values()

print (all_scores)
# -------------------------------


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for x in a:
        print (x)
        if x in b:
                c.append(x)

print (c)


# ----------------convert a list to a set (which is sorted and dupe-removed

testlist = [1,2,2,3,3,3,4,4,4,4,7,7,7,7,5,5,6,6,6]

setlist = set(testlist)

print (testlist)
print (setlist)

# ----------------strings are lists

string = "example"
for c in string:
    print ("one letter: " + c)

