num=int(input("enter the number:"))
i=2
while i<1000:
    i+=1
    if i%num==0:
        continue
    print(i)
