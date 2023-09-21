num=int(input("enter the number:"))
i=1
if num<0:
    print("wrong number entered")
else:
    while i<=num:
        j=1
        while j<=20:
            print(i,"x",j,"=",i*j)
            j+=1
        i+=1
 
