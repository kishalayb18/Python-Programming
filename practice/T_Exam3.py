n=int(input())
p1=0
p2=0
sum=0
a=[]
for i in range(n):
    a.append(int(input()))

for i in a:
    sum=sum+i

if n<2:
    print(0)
else:
    print(sum)