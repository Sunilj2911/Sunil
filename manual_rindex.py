def rindex(string,sub_str,start=0,end=None):
    list1=list(string)
    list1=list1[::-1]
    sub_str=list(sub_str)
    sub_str=sub_str[::-1]
    if end==None:
        end=len(list1)
    for i in range(len(list1)-end-1,len(list1)-start-len(sub_str)):
        if(list1[i:i+len(sub_str)]==sub_str):
            return len(list1)-len(sub_str)-i
       
string=input("Enter the string:")
sub_str=input("Enter the substring you want to search:")
index=rindex(string,sub_str,start=int(input("enter the start index:")),end=int(input("enter the end index:"))) 
print("Index of last occurrence of the substring :",index)      
        
