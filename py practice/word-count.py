import collections
s="hi there how is the day, the day is good now"

arr=s.split()

# newset=list(set(arr))
# print(newset)s

newdict={}
for word in arr:
    if word in newdict:
        newdict[word]+=1
    elif word not in newdict:
        newdict[word]=1
print(newdict)

b=dict(collections.Counter(arr))
print(b)