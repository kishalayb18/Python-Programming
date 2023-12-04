a=[]
n=int(input('no. of chocolates : '))
print('Enter price of chocolates : ')
for i in range(n):
    a.append(int(input()))

b=[]
tempSum=0
temp1=0
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
        x=a.count(a[i])
        y=a[i]
        z=x*a[i]
        
    if z>tempSum:
        tempSum=z
        temp1=y

sum=0
for i in range(len(a)):
    if a[i]!=temp1:
        sum=sum+a[i]

print('Min sum = ',sum)