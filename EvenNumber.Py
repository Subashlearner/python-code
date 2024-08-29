s=input("enter the list of elements")
l=eval(s)
sum=0
print("the even number in the list are")
for i in l:
    if i%2==0:
        sum=sum+i
        print(i)
print("sum of the even number",sum)
    
        
