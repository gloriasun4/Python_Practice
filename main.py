### Array Analysis ###

"""
Given 2 arrays (not duplicates)
Is 1 array a rotation of another - return True/False
same size and elements but start index is different
elements that are cut off at the end get "rotated" to the front

BigO(n) we are going through each array 2x but o(2n) = O(n) since
constants are insignificant

select an indexed position in list2 and get its value. Find same element
in list2 and check index for index from there
if any variation then we know it's false
Getting to the last item without a false means true
"""


def rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    i = 0
    first = list1[0]

    for x in range(len(list2)):
        if list2[x] == first:
            i = x
            break

    if i == 0:
        return False

    for y in range(len(list1)):
        i2 = (i + y) % len(list1)

        if list1[y] != list2[i2]:
            return False

    return True


print(rotation([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(rotation([2, 3, 4], [3, 4, 5]))
print(rotation([34, 78, 19, 20, 33], [20, 33, 34, 78, 19]))
