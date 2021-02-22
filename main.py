import timeit


### Algorithms ###

# sum of numbers from 0 to n inclusive

def sum1(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum += x
    return final_sum


def sum2(n):
    return (n * (n + 1)) / 2


# wrapper function to measure time
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


"""
Objectively comparing two algos
"""
wrapped1 = wrapper(sum1, 100)
wrapped2 = wrapper(sum2, 100)
print(timeit.timeit(wrapped1))
print(timeit.timeit(wrapped2))
# sum1 took 3.6594 seconds, sum2 took 0.2021 seconds
# BUT hardware dependent, time is different on different computers
# Big O Notiation: comparing assignments
