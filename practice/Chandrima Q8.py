#Q8
f=-1
r=-1

def insQ(x):
    queue=x
    max=8
    r=len(queue)-1
    if r<max:
        d=input('Enter 1bit to be inserted: ')
        if len(d)!=1:
            print('only 1 bit data is accepted per insertion')
        else:
            queue.append(d)
            r=r+1
    else:
        print('Overflow')

def delQ(x):
    queue=x
    queue = x
    f = -1
    max = 8
    f = len(queue)
    if len(queue)!=0:
        f=0
        r=len(queue)
    if f!=-1:
        ele=queue[f]
        queue.remove(queue[f])
        f=f+1
        if f==r:
            f=-1
            r=-1
        return ele
    else:
        return 'Underflow'


ip=1
ethernet_pkt_rcvd=0
pcie_pkt_rcvd=0
q=[]
s=input('ip==')
if len(s)>32:
    print('Only 8bits are allowed')
else:
    for i in s:
        q.append(i)
    print(q,len(q))
    if s=='Ethernet Packet':
        ethernet_pkt_rcvd=1
    elif s=='PCIe Packet':
        pcie_pkt_rcvd=1

while ip==1:
    print('1.Print Queue 2.Insert  3.Delete 4.Check Packet Status 5.Exit ')

    ch=int(input('Select an option'))

    if ch==1:
        print(q)
    elif ch==2:
        insQ(q)
    elif ch==3:
        delEle=delQ(q)
        print(delEle)
    elif ch==4:
        print('ethernet_pkt_rcvd= ',ethernet_pkt_rcvd,'pcie_pkt_rcvd= ',pcie_pkt_rcvd)
    elif ch==5:
        ip=0
        print('--exit--')