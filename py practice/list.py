arr=[1,2,3]

#here arr, arr1 will point the same memory
arr1=arr

# arr, arr2 will point to two different memory locations
arr2=arr.copy()

# id of arr, arr1 will be same as they point the same memory
print(arr2, id(arr), id(arr1), id(arr2))

arr[0]=5
print(arr)

#this will change
print(arr1)

# this will not change
print(arr2)