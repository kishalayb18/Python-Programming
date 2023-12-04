#String Pair TCS Codevita 9: Submission by Swapnil Mishra

N = int(input())
numbers = list(map(int, input().strip().split()))

vc=0 #vowel cnt

for i in numbers:
    if i>100:
        print('Error: Greater Than 100')
        break
    if i==100:
        vc=vc+2
        continue
    #dp=decimal place; up=unit place
    dp=i//10
    
    if dp!=0:
        up=i%(10*dp)
    else:
        up=i%10

    if dp==0:
        
        if up==0:
            vc=vc+2
        elif up==1:
            vc=vc+2
        elif up==2:
            vc=vc+1
        elif up==3:
            vc=vc+2
        elif up==4:
            vc=vc+2
        elif up==5:
            vc=vc+2
        elif up==6:
            vc=vc+1
        elif up==7:
            vc=vc+2
        elif up==8:
            vc=vc+2
        elif up==9:
            vc=vc+2
        continue

    elif dp==1:
        if up==0:
            vc=vc+1
        elif up==1:
            vc=vc+3
        elif up==2:
            vc=vc+2
        elif up==3:
            vc=vc+3
        elif up==4:
            vc=vc+4
        elif up==5:
            vc=vc+3
        elif up==6:
            vc=vc+3
        elif up==7:
            vc=vc+4
        elif up==8:
            vc=vc+4
        elif up==9:
            vc=vc+4
        continue
            
    elif dp==2:
        vc=vc+1
    elif dp==3:
        vc=vc+1
    elif dp==4:
        vc=vc+1
    elif dp==5:
        vc=vc+1
    elif dp==6:
        vc=vc+1
    elif dp==7:
        vc=vc+2
    elif dp==8:
        vc=vc+1
    elif dp==9:
        vc=vc+1

    if up==0:
        vc=vc+2
    elif up==1:
        vc=vc+2
    elif up==2:
        vc=vc+1
    elif up==3:
        vc=vc+2
    elif up==4:
        vc=vc+2
    elif up==5:
        vc=vc+2
    elif up==6:
        vc=vc+1
    elif up==7:
        vc=vc+2
    elif up==8:
        vc=vc+2
    elif up==9:
        vc=vc+2
    
        
"""for i in range(N-1):
    print(numbers[i])

print('>j')
for j in range(1,N):
    print(numbers[j])"""
#print('>vc=',vc)

pc=0 #pc=pair count

for i in range(N-1):
    for j in range(i+1,N):
        if numbers[i]+numbers[j]==vc:
            pc=pc+1

#print('>pc=',pc)


if pc==0:
    print('zero')
elif pc==1:
    print('one')
elif pc==2:
    print('two')
elif pc==3:
    print('three')
elif pc==4:
    print('four')

elif pc==5:
    print('five')

elif pc==6:
    print('six')

elif pc==7:
    print('seven')

elif pc==8:
    print('eight')

elif pc==9:
    print('nine')

