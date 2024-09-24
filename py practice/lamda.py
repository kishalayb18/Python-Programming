f = lambda a, b, c : a + b + c
print(f(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def fun(n):
    return n
varfuntion=lambda a:a*fun(2)
print(varfuntion(11))