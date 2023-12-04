"""
Method	            Description

append()	    Adds an element at the end of the list
clear()	            Removes all the elements from the list
copy()	            Returns a copy of the list
count()	            Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()     	    Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	            Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	            Sorts the list
"""

a=[]
a.append(10)
a.append(20)
print(a)
a.clear()
print('Enter 5 elements')
for i in range (5):
    x=input()
    a.append(x)
b=[]
b=a.copy()
print('b=',b)
a=[10,100,1000]
print('a=',a)
a.extend(b)
print('a.extend(b)=',a)
print('index of 1000=',a.index(1000))
a.insert(2,5)
#insert(2,500)
#print('insert(2,500), a=',a)
a.pop(3)
print('pop(3),a=',a)
remove(10)
print('remove(500), a=',a)
a.reverse()
print('a.reverse(), a=',a)
a.sort()
print('a.sort(), a=',a)
