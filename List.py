def new_fun(a):
    s_l=[]
    while a!=[]:
        big_value=a[0]
        for x in a:
             if(big_value<x):
                big_value=x
        s_l.append(big_value)
        a.remove(big_value)
    return s_l
list=eval(input("Enter the list with duplicate elements:"))
print(new_fun(list))
       
