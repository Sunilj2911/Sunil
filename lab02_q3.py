T=int(input())
list=[]
for i in range(1,T+1):
    list.append(int(input()))

for i in list:
    num,count,q=i,0,0
    while(num!=0):
        q=num%10
        if(q==0):
            pass
        else:
          if(i%(num%10)==0):
            count+=1
        num//=10
    print(count)    



