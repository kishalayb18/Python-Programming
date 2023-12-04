ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

twos = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']

N = int(input())
numbers = list(map(int, input().strip().split()))

w=[]
for i in numbers:
    if i>100:
        print('Error: Greater Than 100')
        break
    if i==100:
        sw='Hundred'
        w.append(sw)
        continue
    #dp=decimal place; up=unit place
    dp=i//10

    if dp==0:
        up=i%10
        sw=ones[up]
    elif dp==1:
        up=i%10
        sw=twos[up]
    else:
        up=i%(10*dp)
        if up==0:
            sup=""
        else:
            sup=ones[up]
        sdp=tens[dp]
        sw=sdp+sup
    w.append(sw)

vc=0
for i in w:
    for m in range(len(i)):
        j=i[m]
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            vc=vc+1

pc=0
for i in range(N-1):
    for j in range(i+1,N):
        if numbers[i]+numbers[j]==vc:
            pc=pc+1
            
print(w)

if pc==100:
    y='hundred'
dp=pc//10

if dp==0:
    up=pc%10
    y=ones[up]
elif dp==1:
    up=vc%10
    y=twos[up]
else:
    up=pc%(10*dp)
    if up==0:
        sup=""
    else:
        sup=ones[up]
        sdp=tens[dp]
        y=sdp+sup

print(y)


 
        
