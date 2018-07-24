#Find out how 
#many students are in the list
#Change Lisa’s favourite colour
#Remove 'Jenny' and her favourite colour
#Sort and print students and their favourite colours alphabetically by name

people = {'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
favColor = input("Input new favorite of lisa")

people['Lisa'] = favColor
keyList=[]
del people['Jenny']
print(people)
list1=[]
list1.extend(people)
list1.sort()
for key in list1:
    print(key,':',people[key])
#for key,val in people.items():
    
#print(list1)
