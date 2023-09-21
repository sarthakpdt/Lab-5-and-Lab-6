ch="yes"
i=int(input("enter the number to be divisor:"))
ycount=0
ncount=0
while ch=="yes":
    num=int(input("enter the number:"))
    if num%i==0:
        ycount+=1
    else:
        ncount+=1
    ch=input("do you want to continue?(yes/-999):")
print("the total number that are divisible are:",ycount)
print("the total number that are not divisible are:",ncount)        
