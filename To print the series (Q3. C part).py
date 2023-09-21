num=int(input("enter the number:"))
x=int(input("enter the value of numerator:"))
fact=1
i=0
sum=0
f1=x
f2=(-(x**2)/2)
while i<=num:
    fact=fact*i
    i+=2
while (f2-f1 < num):
    sign=(-1)**i
    sum+=(f2-f1)+((x**(2*i+1)))/fact*sign
print(sum)
