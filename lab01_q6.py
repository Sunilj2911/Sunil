
list=[]
ans=[]
for t in range(10):
    co_ord=[]
    print("Enter the coordinates of",t+1,"point")
    for u in range(3):
        co_ord.append(int(input()))
    list.append(co_ord) 
print(list)
for el in list:
    min_dist=10000
    dist=0
    temp_ans=[0]
    for i in list:
        if i!=el:
            dist=(((el[0]-i[0])**2)+((el[1]-i[1])**2)+((el[2]-i[2])**2))**0.5
            if min_dist>dist:
                min_dist=dist
                temp_ans[0]=i
    ans.append(temp_ans)        
            
print("Nearest points are :",ans)  
  
        
       