tc=int(input())
arr=[]

while tc>0:
    arr.clear()
    s=""
    cnt=1
    n=int(input())
    arr=input().split(" ",maxsplit=n)
    for ele in arr:
        s=s+ele
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            cnt=cnt+1
    print(cnt)

    tc=tc-1