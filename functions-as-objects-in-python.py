# Functions can be passed as arguments

# We define an 'apply' function which will take as input a list, _L_ and a function, _f_ and apply the function to each element of the list.

def apply(L, f):
    """
    Applies function given by f to each element in L
    Parameters
    ----------
    L : list containing the operands
    f : the function
    Returns
    --------
    result: resulting list
    """

    result = []
    for i in L:
        result.append(f(i))

    return result

L = [1, -2, -5, 6.2]
a = apply(L, abs)
print(a)    # [1, 2, 5, 6.2]
# abs is applied on elements passed in L

a = apply(L, int)
print(a)    # [1, -2, -5, 6]

# We can also pass a self-defined function. For example:
def sqr(num):
    return num ** 2

a = apply(L, sqr)
print(a)    # [1, 4, 25, 38.440000000000005]

# The ability to perform the same operation on a list of elements is also provided by a higher-order python function called __map__.
# In its simplest form, it takes in a 'unary' function and a collection of suitable arguments and returns an 'iterable' which we must walk down.
for i in map(abs, L):
    print(i)

# Functions as elements of a list
# Functions can be stored as elements of a list or any other data structure in Python. For example, if we wish to perform multiple operations to a particular number, we define `apply_func(L, x)` that takes a list of functions, L and an operand, x and applies each function in L on x.
from math import exp

def apply_func(L,x):
    result = []
    for f in L:
        result.append(f(x))
    return result

function_list = [abs, exp, int]
print(apply_func(function_list, -2.3))
print(apply_func(function_list, -4))

# Side Note: In both the above examples, we could have used list comprehensions, which provide an elegant way of creating lists based on another list or iterator.
output = [f(-2.3) for f in function_list]
print(f'output: {output}')