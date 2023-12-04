t=int(input('>>'))
tcase=1

a=[]
b=[]
c=[]

while t>=tcase:
    total = 0
    num=0
    treat=1
    n=int(input())
    x=input()
    for i in x.split(' ',n):
        a.append(int(i))

    for i in a:
        if i not in b:
            b.append(i)
    b.sort()

    for i in b:
        num=a.count(i)
        total=total+(num*treat)
        treat=treat+1
        num=0

    c.append(total)
    print('#', tcase, ': ', total)
    tcase=tcase+1
    a.clear()
    b.clear()
#
#
# for i in range(len(c)):
#     print('#',i+1,': ',c[i])