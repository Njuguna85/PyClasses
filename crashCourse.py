# functions
def sayHello(name):
    """ 
        A function that takes in an argument and prints it
        """
    print('Hello ' + name, "!!!")


sayHello('Dennis')


def getSum(x, y):
    sum = x + y
    return sum


print(getSum(234, 324))

"""
    Lambda function
    A lambda function is a function that can take any number of arguments,
    but can only have one expression and is similar
    to JS arrow functions

"""


def getMulti(num1, num2): return num1 * num2


print(getMulti(123, 123))


# Comparison operator

x = 132
y = 123

if x == y:
    print(f'{x} is equal to {y}')
elif x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')


# in
numbers = [1, 2, 3, 4, 5]
x = 4
if x in numbers:
    print(x in numbers)

"""
    loops.. 
    for loops and while loops
"""

# For Loop

people = ['Dennis', 'Duncan', 'Daniel', 'Janet']

for person in people:
    print('My name is ', person)
