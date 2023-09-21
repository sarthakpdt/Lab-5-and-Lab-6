num=int(input("enter the number:"))
i=0
while i<num:
    sp=num-i-1 
    while sp>0:
        print(end=" ")
        sp-=1
    star=i+1
    while star>0:
        print("*",end=" ")
    star-=1
    i+=1
    print()
    
    
