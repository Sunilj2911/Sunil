list1=[]
for i in range(50):
    list1.append(i)
list2=[]    
for t in range(1,51):
    list2.append(t**2) 
list3=[]
character=97
for u in range(1,27):
    text=(u*chr(character))
    list3.append(text)
    character+=1 
print(list1)  
print(list2)
print(list3)            