count=int(input("How many numbers you want to take HCF:")) 
while count<=0: 
     print("Invalid input") 
num=int(input("enter the number:"))
if num<0:
    print("invalid input")
i=1 
while i<count: 
     n=int(input("enter number:")) 
     if n<=0: 
         print("Invalid input")  
     else: 
         while n: 
             temp=num 
              num=n 
             n=temp%n   
         i+=1 
print("HCF of given numbers is:",num)
