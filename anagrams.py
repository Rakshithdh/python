a=input("str1")
b=input("str2")

str1=sorted(a.lower())
str2=sorted(b.lower())


print(str1,str2)

if str1==str2:
    print('yes')
else:
    print("no")