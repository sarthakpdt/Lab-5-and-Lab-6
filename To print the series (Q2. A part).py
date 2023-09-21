num=int(input("enter the number:"))
total=0
i=1
while i<=num:
    total+=(1/i)
    i+=1
print("the sum of the series is:",round(total,9))
