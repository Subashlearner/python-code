def fib(n):
    if n<1:
        return None
    if n<3:
        return 1
    else:
      return fib(n-1)+fib(n-2)
n=int(input("enter the number:"))
for i in range(n):
 print(fib(i))
