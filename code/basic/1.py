# Add Two Numbers with “+” Operator
a = 10
b = 10
sum = a + b
print("The Sum of {0} and {1} is {2}".format(a, b, sum))
print('*'*120)


# Python program to add two numbers
def twonum(a,b):
    # c = a + b
    return a + b

a = 10
b = 10
result = twonum(a, b)
print("The sum of {0} and {1} is {2}".format(a,b,result))
print('*'*120)

# Add Two Numbers Using operator.add() Method
import operator

a = 10
b = 10
result = operator.add(a,b)
print("The sum of {0} and {1} is {2}".format(a,b,result))
print("*"*120)

# Add Two Number Using Lambda Function

add_num = lambda a,b: a + b

a = 10
b = 10
result = add_num(a,b)

print("The sum of {0} and {1} is {2}".format(a,b,result))