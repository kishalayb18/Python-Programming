s = input('enter a sentence')
arr=s.split()

for i,word in enumerate(arr):
    # print(i,word)
    arr[i]=word[::-1]
# for word in arr:
#     word=word[::-1]

s=" ".join(arr)
print(s)