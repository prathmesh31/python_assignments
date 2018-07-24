#pangram
pangram = input("Enter a pangram").lower()
panList=[]
for i in range(len(pangram)):
    if pangram[i].isalpha():
        panList.append(pangram[i])
panSet = set(panList)
print(panSet)
if len(panSet) == 26:
    print("Pangram")
else:
    print("Not pangram")
    
