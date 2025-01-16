test = int(input())
no_of_boxes = int(input())
swap = int(input())
x = int(input())

while swap!=0:
    a = int(input())
    b = int(input())
    
    if x==a:
        x=b
    elif x==b:
        x=a
    
    swap-=1
print("The coin is in",x)
