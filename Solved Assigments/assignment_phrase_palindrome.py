#palindrome paragraph
#"Go hanga salami I'm a lasagna hog.", "Was it a rat Isaw?", 
#"Step on no pets", "Sit on a potato pan, Otis", "LisaBonet ate no basil",
#"Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
#"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation,
#capitalization, and spacing are usually ignored.

phrase = input("Enter a palindrome phrase")
temp=""

for i in range(len(phrase)):
    if phrase[i].isalpha():             #exculdes symbols
        temp+=phrase[i]                 #This will add charcter only one by one
if temp.lower() == temp[::-1].lower():  #condition for palindrome
    print("palindrome")
else:
    print("not palindrome")
