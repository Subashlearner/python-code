
def checkleap(y):
  if 1600<=y<=9999:
    if y%100==0 :
      return y%400==0
    else:
      return y%4==0
  else:
    return False
y=int(input("enter the year:"))
if checkleap(y):
        print("leap year")
else:
        print("not a leap year")
