import random
values=[0,1]
list=[]
for i in range(100):
    list.append(random.choice(values))
print(list)    
max_count,count=0,0
for el in list:
    if el==0:
        count+=1
    else:
        if max_count<count:
            max_count=count
        count=0
print(max_count)                
    
    
