### Challenges ###
# source: https://www.w3resource.com/python-exercises/challenges/1/index.php

"""
20. Write a Python program to check a sequence of numbers is an arithmetic progression or not.
Input : [5, 7, 9, 11]
Output : True
In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.
"""


def arith_progression(lst):
    if len(lst) < 2:
        return False
    diff = lst[1] - lst[0]

    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != diff:
            return False

    return True


print(arith_progression([5, 7, 9, 11]))
