# python_assignments
Repository of all Assigments of python module of CDAC PG-DBDA Course

The assignments are as follows:

Day1:

1. Write a tax calculator by using python Accept annual income,
investments done by a person Annual income – investments = taxable income 
Ask user Any loan taken. 
If yes then accept principle amt of loan Taxable 
principle loan = new taxable income 
Calculate tax using following slabs 
<2.5 	lakhs						no tax 
2.5 	lakhs 	and <= 5 lakhs then 10% 
>5	lakhs  	and < 10 lakhs then 20% 
Else 30% 

2. Accept marks for 6 subjects from user, calculate percentage  and display grade 
Less than 50	fail 
>=50&<=60  	third 
>60&<=70 		second 
>70&<=80  		first 
Else distinction 

3 . Write a program that asks the user how many days are in a particular month, 
and what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), 
and then prints a calendar for that month. 
For example, here is the output for a 30day month that begins on day 4 (Thursday):
S	M	T	W	T	F	S                
	1	2	3	4	5	6 
7	8   9	10	11	12	13 
14 	15	16	17	18	19	20
21	22	23	24	25	26	27
28	29	30 

4.  Display
         
   	1		1                
	1 1		1 3
	1 1 1		1 3 5
 
5.  Accept a string from user Accept another string from user Check whether substring if yes display position Then accept 2 numbers from user Splice the string at that position Accept a character from user Split the  string at the character Display 
string in uppercase and lowercase 

6.  Ask user how many numbers you want to enter accept those many numbers from user and
find addition, average, min and max values for the given list. 

7. Accept a number from user and find addition of digits of number 

8. Accept a string from user and check whether it is palidrom 
 
9. Q. 2. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following: 
**** 
********* 
******* 
 
Q. 3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hanga salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa 
Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", 
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and 
spacing are usually ignored. 

Q. 4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for 
example: The quick brown fox jumps over the lazy dog.  
Your task here is to write a function to check a 
sentence to see if it is a pangram or not. 
 
Q5.In cryptography, a Caesar cipher is a very simple encryption techniques 
in which each letter in the plain text is replaced by a letter some fixed number of positions down 
the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. 
The method is named after Julius Caesar, who used it to communicate with his generals. 
ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. 
In Python, the key for ROT-13 may be represented by means of the following dictionary:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t',
	'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 
	'o':'b','p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
	'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
	'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B',
	'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K',
	'Y':'L', 'Z':'M'}

Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read the following secret message: Pnrfnepvcure? V zhpucersrePnrfnefnynq! Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written in English. 
 
 
Day 3 
 
Q. 1. Given a dictionary of students and their favourite colours: 
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
Find out how many students are in the list Change Lisa’s favourite colour 
Remove 'Jenny' and her favourite colour Sort and print students 
and their favourite colours alphabetically by name 

Q2. Write a function translate() that will translate a text into 
"rövarspråket" (Swedish for "robber's language").
 That is, double every consonant and place an occurrence of "o" in between.
 For example, translate("this is fun") should return the string "tothohisosisosfofunon". 

 
Day4: 
 
Q. 2. Write a program that contains a function that has one parameter, n, representing an integer greater than 0. The function should return n! (n factorial). Then write a main function that calls this function with the values 1 through 20, one at a time, printing the returned results. This is what your output should look like: 1 1 2 2 3 6 4 24 5 120 6 720 7 5040 8 40320 9 362880 10 3628800 
 
Q. 3. We can define sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer 
x > 1: 1, 
if x = 1 x + sum from 1 to x-1 
if x > 1 Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 
recursively: 
def main(): 
compute and print 1 + 2 + ... + 10 
print sum(10) 
def sum(x): 
you complete this function recursively main()

Q. 4. Define a function overlapping() that takes two lists and returns True if they have at least one member in common, 
False otherwise. 

Q. 5. Write a function find_longest_word() that takes a list of words and returns 
the length of the longest one. 

Q. 6. Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n 
Q. 7. Define a simple "spelling correction" function correct() that takes a string and sees to it that 
1) two or more occurrences of the space character is compressed into one, and 
2) inserts an extra space after a period if the period is directly followed by a letter. 
e.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool. Indeed!" 

Q. 8. In English, present participle is formed by adding suffix -ing to infinite form: 
go > going. A simple set of heuristic rules can be given as follows: 
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing For words consisting of consonant-vowel-consonant,
double the final letter before adding ing By default just add ing Your task in this exercise is to 
define a function make_ing_form() which given a verb in infinitive form returns its present participle form. 
Test your function with words such as lie, see, move and hug. 