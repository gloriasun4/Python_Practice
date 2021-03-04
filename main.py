### Array Common Elements ###

"""

Common Elements in Two Sorted Arrays
return a sorted array of the common elements between two sorted arrays of integers
Ex: [1,3,4,6,7,9] and [1,2,4,5,9,10] would return [1,4,9]

"""


def common_elements(a, b):
    p1 = 0
    p2 = 0

    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 1
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1

    return result


print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))
print(common_elements(sorted([2, 3, 456, 8, 2, 34, 6, 78, 19, 23, 4]), [1, 2, 4, 5, 9, 10]))
