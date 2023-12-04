mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

#USING USER DEFINED FUNCTION
"""
def my_function(x):
  return list(dict.fromkeys(x))

a=["a", "b", "a", "c", "c"]
mylist = my_function(a)

print(mylist)
"""
