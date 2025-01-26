def replace(string,old_str,new_str):
    list1=list(string)
    for i in range(len(string)-len(old_str)):
        if(list1[i:i+len(old_str)]==list(old_str)):
            list1[i:i+len(old_str)]=list(new_str)
    return ''.join(list1)   
string=input("Enter the string:")
old_str=input("Enter the substring you want to replace:")
new_str=input("Enter the substring you want to add:")
print("The updated string:",replace(string,old_str,new_str) ) 
