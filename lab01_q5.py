list1=[]
list2=[]
list3=[]
for i in range(15):
    list1.append(input())
for el in list1:
    list2.append(el[0:15])
print(list2)
for t in list2:
    list3.append(t[::-1])
print(list3)   
   