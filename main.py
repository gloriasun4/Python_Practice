import timeit
from math import log

### Array Sequences ###

# Lists, Tuples, and Strings all support indexing

""" Memory is stored in bits, there are 8 bits in a byte. UNICODE characters take 2 bytes each.
All stored in a memory location. stored and retrieved in constant O(1) time"""

# When creating a list that is part of another list, a new list is NOT created in memory.
# The indexes change/ changing and creating pointers.

lst = [2, 3, 5, 7, 11, 13, 17, 19]
temp = lst[3:6]
print(temp)

# When assigning new value, the index just points to a new location in memory, does not change lst
temp[2] = 15
print(temp)

# TODO sys api and .format()
import sys

n = 10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)

    print("Length: {0:3d}; Size in bytes: {1:42} ".format(a, b))

    data.append(n)

# takeaway: when initially declared, python makes some space for an empty array. once that array is filled up,
# will assign a bigger array that point to the same values, then delete the original array, and make the
# new array the "original" one. this process repeats as you add more values
