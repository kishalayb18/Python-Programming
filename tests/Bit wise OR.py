tc=int(input())
bw=[]
ar=[]
while tc>0:
    
    N = int(input())
    num = list(map(int, input().strip().split()))

    v=num[0]
    for j in range(1,N):
        v=v|num[j]

    cnt=0
    for i in range(N-1):
        for j in range(1,N):
            k=num[i]|num[j]
            if k==v:
                cnt=cnt+1
        
    tc=tc-1
    
print(cnt)

