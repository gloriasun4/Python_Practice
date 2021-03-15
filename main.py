### Challenges ###
# source: https://www.w3resource.com/python-exercises/challenges/1/index.php

"""
31. Write a Python program to add two binary numbers.
Input : ('11', '1')
Output : 100
"""


def add_bin(b1, b2):
    b1_digit = b1 % 10
    b2_digit = b2 % 10
    b1_num = b1[:-1]
    b2_num = b2[:-1]
    sum = 0
    carry = 0
    while len(b1_num) > 0 & len(b2_num) > 0:

        if b1_digit == 1 & b2_digit == 1:
            carry = 1

    return sum

# solution

def add_binary_nums(x, y):
    max_len = max(len(x), len(y))

    x = x.zfill(max_len)
    y = y.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0: result = '1' + result

    return result.zfill(max_len)


print(add_binary_nums('11', '1'))
print(add_binary_nums('10', '10'))
print(add_binary_nums('111', '111'))
print(add_binary_nums('1111111', '1'))

"""
31b. Write a Python program to add two binary numbers (into decimal).
Input : ('11', '1')
Output : 100
"""


def add_bin2(b1, b2):
    return int(b1, 2) + int(b2, 2)


print(add_bin2('11', '1'))
