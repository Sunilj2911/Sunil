def count(string,sub_str,start=0,end=None):
    count=0
    if end==None:
        end=len(string)
    for i in range(start,end-len(sub_str)):
        if(string[i:i+len(sub_str)]==sub_str):
            count+=1
    return count    
string=input("Enter the string:")
sub_str=input("Enter the substring you want to count:")
count=count(string,sub_str,start=int(input("enter the start index:")),end=int(input("enter the end index:"))) 
print("count of the substring in the string :",count)      
        
    