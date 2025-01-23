num=int(input("Enter the number:"))
q=0
old_num=num
ans=0
while num!=0:
    q=num%10
    ans=(10*ans)+q
    num//=10
print("Reverse of",old_num,":",ans)    
    
