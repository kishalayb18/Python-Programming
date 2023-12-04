a=[]
m=int(input('m= '))
k=int(input('k= '))
v=2
a.append(v)
while k>0:
    x=((v+1)%m)
    a.pop(0)
    for i in range(x):
        a.append(i)
    k=k-1
    v=a[0]
print(len(a))
print(a)
