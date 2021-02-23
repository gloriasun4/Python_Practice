import timeit
from math import log
"""
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('bmh')
"""

### Algorithms ###

# sum of numbers from 0 to n inclusive

# def sum1(n):
#     final_sum = 0
#     for x in range(n + 1):
#         final_sum += x
#     return final_sum
#
# The big O-notation would be O(n) (the 1 doesn't matter as n becomes infinitely big)
#
# def sum2(n):
#     return (n * (n + 1)) / 2
#
#
# # wrapper function to measure time
# def wrapper(func, *args, **kwargs):
#     def wrapped():
#         return func(*args, **kwargs)
#
#     return wrapped


"""
Objectively comparing two algos
"""
# wrapped1 = wrapper(sum1, 100)
# wrapped2 = wrapper(sum2, 100)
# print(timeit.timeit(wrapped1))
# print(timeit.timeit(wrapped2))
# sum1 took 3.6594 seconds, sum2 took 0.2021 seconds
# BUT hardware dependent, time is different on different computers
# Big O Notation: comparing assignments
""" Big-O notation describes how quickly runtime will grow relative to the input
as the input gets arbitrarily large
We are trying to describe the limiting behavior, asymptotic analysis"""


def big_o(n):
    return 45 * n ** 3 + 20 * n ** 2 + 19

big_o(1)
big_o(10)

# O(n^3)

""" Different Types, scaled by runtime graphs
O(1) constant
O(log log n)) double logarithmic
O(log n) logarithmic
O(n^c) 0 < c < 1 fractional power
O(n) linear
O(nlog*n) n log-star n????
... many more

"""
