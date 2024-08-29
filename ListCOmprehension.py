n=int(input("enter the input value"))
l1=[3*x for x in range(0,n)]
print(l1)
l2=[x for x in l1 if x%2==0]
print(l2)
