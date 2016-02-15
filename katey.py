

for i in range(1,10):
    print ("Hello Katey")

for i in range(1,100):
    print ("i = ", i, "i+9 = ", i+9)



def add_numbers (args):
    total = 0
    for z in args:
        total += z
    print("Add_numbers total is : ", total)
    print(args)
    print(args[3])

numlist = (1,2,34,54,5,43,3,5,4,3,2,3,4,565,4,3,3,3)

add_numbers (numlist)