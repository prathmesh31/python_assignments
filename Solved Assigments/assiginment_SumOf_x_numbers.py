#sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1
#1. if x = 1
#   x + sum from 1 to x-1 if x > 1
#Complete the following Python program to compute the sum
#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively:
#def main():
# compute and print 1 + 2 + ... + 10
#print sum(10)
#def sum(x):
# you complete this function recursively main()

def sum(x):
    try:
        if x <= 0:
            raise ValueError("Please enter number greater than 0")
    except ValueError:
        x = int(input("Enter a value grater than 0 please "))
        return sum(x)               #otherwise it will return 1
    if x>1:
        print(x,"+",end="")
        return x+sum(x-1)
    else:
        print(x)
        return 1

sumNum = int(input("Enter a number grater than 0"))
print( "Sum is",sum(sumNum))
