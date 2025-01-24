word=input("Enter the word:")
list=[]
for i in range(len(word)):
    if(i%2!=0):
        list.append(word[i].upper())
        
    else:
        list.append(word[i].lower())
print(''.join(list))            
