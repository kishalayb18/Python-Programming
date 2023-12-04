str=[]
n=int(input())
for i in range(n):
    str.append(input())

def Alice_str(s):
    cnt1=0
    cnt2=0
    flag=0
    temp=''
    for i in s:
        cnt1=0
        for j in range(len(i)):
            temp=i[j]+temp
        for k in range(len(i)):
            if i[k]!=temp[k]:
                cnt1=cnt1+1
        if cnt1<=2:
            cnt2=cnt2+1
    return cnt2

op=Alice_str(str)
print(op)

