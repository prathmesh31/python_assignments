#Write a function translate() that will translate a text into "
#rövarspråket" (Swedish for "robber's language").
#That is, double every consonant and place an occurrence of "o" in between.
#For example, translate("this is fun") should return the string "tothohisosisosfofunon".

str1 = 'this is fun'
vowels = ['a','e','o','i','u']
robberLang=""
for char in str1:
    if char.isalpha():
        if char in vowels:
            robberLang+=char
        else:
            robberLang+=char+'o'+char
print(robberLang)

