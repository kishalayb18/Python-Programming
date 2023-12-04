# n=int(input('Enter array size: '))
# print('Enter elements:')
# #for i in range(n):
# a=[int(input())for i in range(n)]
# min=a[0]
# max=a[0]
# for i in a:
#     if min>i:
#         min=i
#     if max<i:
#         max=i
# print('The array is-')
# print(a)
# print('Min=',min)
# print('Max=',max)

a=[1,2,3,4,5,6]

a[0:3]=reversed(a[0:3])

print(a)

