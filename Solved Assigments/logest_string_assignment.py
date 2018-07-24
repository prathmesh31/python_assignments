#Write a function find_longest_word() that takes a list of words and returns the 
#length of the longest one.

import functools #for reduce function
def longest(agrs=[]):
    print(functools.reduce(lambda x,y:x if (len(x)>len(y)) else y,agrs))
    return len(functools.reduce(lambda x,y:x if (len(x)>len(y)) else y,agrs))
#end of function

#main block

mylist = ['HHAAAAAAAAAAAAAAAAAAAAAAAA','prath','prathmesh']
print(longest(mylist))
    
