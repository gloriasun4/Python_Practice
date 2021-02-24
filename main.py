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


func_linear([1,2,3,4])
# the larger the list, the bigger the BigO, scales linearly with n