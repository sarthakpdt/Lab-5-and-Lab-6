num=int(input("enter the number:"))
x=int(input("enter the value of numerator:"))
fact=1
i=1
sum=0
f1=x
f2=(-(x**3)/6)
while i<=num:
    fact=fact*i
    i+=2
while ((f2-f1) < num):
    sign=(-1)**i
    sum+=((x**(2*i+1)))/fact*sign
print(sum)
