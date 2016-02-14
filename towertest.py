first = 0
second = 0
third = 1

n=100

triblist = [first,second,third]

for i in range(0,n):

    trib = first + second + third

    triblist.append(trib)


    print (triblist)

    first = second
    second = third
    third = trib



    # if first == 0:
    #     triblist[0] = str(first)
    #
    # if second == 0:
    #     triblist.append(second)
    #
    # print (triblist)




