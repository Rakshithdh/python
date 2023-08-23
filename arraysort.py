n=int(input("size of array"))
arr=[]
evenarray=[]
oddarray=[]
for i in range(1,n+1):
    userinput=int(input("enter array"))
    arr.append(userinput)
    if i % 2 == 0:
        evenarray.append(arr[i])
    else:
        oddarray.append(arr[i])

print(arr)
print(evenarray)
print(oddarray)

a=evenarray[-2]
b=oddarray[-2]
sum=a+b

print('sum of 2 lqargest no', sum)







