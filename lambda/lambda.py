# lambda arguments : expression
# A lambda function is a small anonymous function.

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a + b
print(x(5,9))

x = lambda a, b, c: a+b+c
print(x(5,8,6))

def myfunc(n):
    return lambda a: a*n

mydoubler = myfunc(2)
print(mydoubler(11))