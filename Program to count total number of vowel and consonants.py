sen=input("enter the sentence:")
lst=["a","e","i","o","u","A","E","I","O","U"]
vcount=0
count=0
sp=0
word=0
for i in sen:
    if i in lst:
        vcount+=1
    elif i==" ":
        word+=1
    else:
        count+=1
for i in range(0,len(sen)):
    if sen[i]==" ":
        sp+=1
print("the total number of vowels are:",vcount)
print("the total number of consonats are:",count-sp)
print("the total number of words are:",word+1)
    
