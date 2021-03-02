### Largest Sum ###

""" Take an array with positive and negative integers
and find the largest continuous sum"""


def largest(arr):
    if len(arr) == 0:
        print('Too small!')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(largest([32,46,567,-435,3,64]))

### Reversing a String ###


""" 
Given a string of words, reverse all the words

start = "This is the best
finish = best the is This
"""

# built in python function
# " ".join(reversed(s.split()))
# " ".join(s.split()[::-1])
# start, stop, end. if both start and stop are :,
# then go from beginning to end or vice versa


def reverse(s):
    length = len(s)
    i = 0
    words = []
    spaces = [" "]

    while i < length:
        if s[i] not in spaces:
            start = i
            while i < length and s[i] not in spaces:
                i+=1
            words.append(s[start: i])
        i+=1

    return " ".join(reversed(words))

print(reverse("This is the best"))