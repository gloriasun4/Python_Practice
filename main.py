import timeit
from math import log


### Algorithms ###

# O(1) constant
# prints first element in a list


def func_constant(values):
    print(values[0])


func_constant([1, 2, 3, 4, 5, 6, 7, 8])


# no matter how large the list, will always return only the first element

# O(n) linear
# takes in a list and prints all values


def func_linear(values):
    for x in values:
        print(x)


func_linear([1, 2, 3, 4])


# the larger the list, the bigger the BigO, scales linearly with n

# O(n^2) quadratic
# prints pairs for every element in list


def func_quad(values):
    for x in values:
        for y in values:
            print(x, y)


func_quad([1, 2, 3])
""" algo operates n times n assignments, so for a length 3 list, 3^2 is 9
two loops, one nested inside the other"""


# Calculating the Scale of Big O
# insignificant terms drop out of the notation
# like taking limits of n to infinity

# Algo with 3n operations is O(n). constants are insignificant because 3(infinity) is the same as infinity

# Example algo with O(1 + n/2 + 10) is just O(n/2)


def func_linear_mix(values):
    print(values[0])

    mid = len(values) // 2
    for x in values[:mid]:
        print(x)

    for x in range(10):
        print("Hello")


func_linear_mix([1, 2, 3, 4, 5, 6, 7, 8])
