def permuta(n):
    if n==0 or n==1:
        return 1
    else:
        sum=1
        for i in range(1,n+1):
            sum=sum*i
        print(">",sum)
        return sum

n=int(input())
x=int(input())
x1=n-1-x-1
if 2<=n<=1000000000 and 2<=x<=1000000000:
    a=permuta(n-1)
    b=permuta(x1)
    c=a//b
    d=c%1000000007
    print(d)