num=int(input("enter the number:"))
fact=1
i=1
sum=0
while i<=num:
    fact=fact*i
    i+=1
    sum+=1/fact
print("the sum of the series is:",round(sum,9))
