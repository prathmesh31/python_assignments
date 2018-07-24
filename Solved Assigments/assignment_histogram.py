#histogram
numOfArgs = int (input ("Enter number of argument of histogram") )
if numOfArgs>0:
    histogram = []  #for empty list
    for i in range(numOfArgs):  #for loop till number of arguments i.e no of elements
        histogram.append(int(input( "Enter the first argument of histogram"))) #for entering list elements
    for x in histogram:
        for y in range(x):
            print("*",end="")
        print(" ")
