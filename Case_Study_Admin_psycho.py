N=int(input())
list=[]
swap=0
for i in range(N):
    list.append(int(input()))
for t in range(N):
    if((t+1)!=list[t]):
        for u in range(N):
            if (list[u]==t+1):
                list[t],list[u]=list[u],list[t]
                swap+=1
 print(swap)
