### Array Algorithms ###

'''
Array Pair Sum
Given an integer array, output all the unique pairs that sum up to a specific
value k.
'''


def pair_sum(array, k):
    if len(array) <= 1:
        print('Too small')

    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)
# should return (1, 3) and (2, 2)
