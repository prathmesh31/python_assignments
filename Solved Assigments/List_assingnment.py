#Take number of elements of list from user
#input list element
#show sum,average,min,max of elements given list

numOfElem=int(input("Enter no of elements of list"))
list1=[]
sum=0
for i in range(numOfElem):
    list1.append(int(input("Enter elements of list: ")))
    sum+=list1[i]

print("Maxium of list is",max(list1))
print("Minimum of list is",min(list1))
print("Sum of elements of list is",sum)
print("average of list is",(sum/len(list1)))
