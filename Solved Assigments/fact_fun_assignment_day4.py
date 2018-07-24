"""Write a program that contains a function that has one parameter, n, representing an integer greaterthan 0.
The function should return n! (n factorial).
Then write a main function that calls this function with the values 1 through 20,
one at a time, printing the returned results. This is what
your output should look like:
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800"""
def factFun ():
    n = int(input("Enter a number for factorial calculation"))
    fact=n
    try:
        if n == 0:
            raise ValueError("Please enter vaule grater than 0")
    except ValueError as e:
        factFun()
    for i in range(fact):
        if i > 1:
            fact*=i;
    print(n,fact)

for i in range(1,21):
    factFun()
        
        
