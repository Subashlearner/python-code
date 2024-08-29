l=[1,2,3,4,5,4,4,4,6,6,6,6,6,7]
x=int(input("Enter the number to check occurance of the element"))
count=0
for i in l:
    if i==x:
        count+=1
if count>0:
    print(x,"the number occured",count,"times")
else:
    print("the number not in the list")
