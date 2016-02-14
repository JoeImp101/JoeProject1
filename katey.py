

for i in range(1,10):
    print ("Hello Katey")

for i in range(1,10):
    print ("i = ", i, "i+9 = ", i+9)



def add_numbers (*args):
    total = 0
    for z in args:
        total += z
    print("Add_numbers total is : ", total)
    print(args)
    print(args[3])

add_numbers (1,1,1,1,1,1,1,1)