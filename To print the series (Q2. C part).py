num=int(input("enter the number:"))
x=int(input("enter the numerator:"))
sum=0
i=1
while i<=num:
    sum+=(1+(x**i)/i)
    i+=1
print("the sum of the series is:",round(sum,9))
