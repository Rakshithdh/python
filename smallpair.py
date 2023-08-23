def Productsmallpair(sum,arr):
    sarr=[]
    size=int(input("size"))
    for i in range(0,size):
        n=int(input("number"))
        arr.append(n)
    sarr=sorted(arr)
    print(sarr)
    add=sarr[0]+sarr[1]
    if add<sum:
        print(sarr[0]*sarr[1])
    else:
        return 0
arr=[]
Productsmallpair(4,arr)
