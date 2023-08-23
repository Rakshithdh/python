m=100
n=161

def calculate(m,n):
    ans=0
    for i in range(m,n+1):
        if i%3==0:
        
            if i%5==0:
                ans+=i
    print(ans)

calculate(m,n)