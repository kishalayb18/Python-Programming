s=input()
a=s.split(' ')
a1=[]
for i in a:
    a1.append(int(i))
def MaxInArray(arr):
    max=0
    mi=0
    for i in range(0,len(arr)):
        if max<arr[i]:
            max=arr[i]
            mi=i
    print(max)
    print(mi)
MaxInArray(a1)