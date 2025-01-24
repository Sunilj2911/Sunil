dict={}
items=int(input("enter the no. of products required:\t"))
for i in range(items):
    prod=input("enter the product name:\t")
    price=int(input("enter the product price:\t"))
    dict[prod]=price
print("enter Done for exit:")
while(True):
    result=input("enter the product name:\t")
    if(result=="Done"):
        exit()
    else:
        print("product price is=",dict[result])
 