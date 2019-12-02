# Python map() function

# __map()__ function returns a list of the results after applying the given function to each item of a given iterable (list, tuple, etc.)

# Code 1: Python program to demonstrate working of map.
# Return double of n
def addition(n):
    return n + n
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Code 2: We can also use lambda expressions with map to achieve above result.
# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Code 3: Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# Code 4: List of strings
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of string individually
test = list(map(list, l))
print(test)

x = list('hello world!')
x = x[:5] + x[6:]
print(x)