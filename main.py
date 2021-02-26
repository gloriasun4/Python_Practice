import timeit
from math import log


### Algorithms ###

# Worst Case vs Best Case: can have very different Big-O times


def matcher(lst, match):
    for x in lst:
        if x == match:
            return True
    return False


# Best case, item is at index one, O(1) constant
matcher([1, 2, 3, 4, 5], 1)
# Worst case, all indexes must be searched O(n) linear
matcher([1, 2, 3, 4, 5], 6)


# Space Complexity

def memory(n):
    for x in range(n):  # O(n) time-wise / time complexity
        print("Hello!")  # O(1) memory-wise/ space complexity: only stores one string


memory(10)

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
