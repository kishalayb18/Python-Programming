import math
arr=[]
temp=[]
def isHappy(n) -> bool:
    flag=-1
    sum=0
    temp.append(n)
    for digit in str(n):
        arr.append(int(digit))
    for i in arr:
        sum = sum + pow(i,2)
    arr.clear()
    print(temp)
    n=sum
    if sum == 1:
        print("isHappy")
        flag=1
    elif n in temp:
        #print("false")
        flag=0
    else:
        isHappy(n)

    if flag == 0:
        return False
    if flag == 1:
        return True
    
print(isHappy(19))



