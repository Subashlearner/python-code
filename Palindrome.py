word1 = input("enter the string:")
N1 = len(word1)
mid = int(N1 / 2)
j=-1
i=0
for x in range(mid):
    if word1[i] != word1[j]:
        print("not a palindrome")
        break
    i+=1
    j-=1
else:
     print("Palindrome")
