n=int(input("enter number"))
m=int(input("enter number"))

divno=[]
nondivno=[]

def differenceofsum(n,m):
    for i in range(0,m+1):
        if i%n==0:
            divno.append(i)
            sumdivno=sum(divno)

        if i%n!=0:
            nondivno.append(i)
            sumnondivno=sum(nondivno)
        
    print(divno)
    print(sumdivno)
    print(nondivno)
    print(sumnondivno)
    print(sumnondivno-sumdivno)

differenceofsum(n,m)