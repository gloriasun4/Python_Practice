### Non-Repeat Elements ###

"""
Take a string and return character that never repeats
if multiple uniques then return only the first unique
"""


# just returning the first unique character

# def unique(s):
#     s = s.replace(" ", "").lower()
#     chars = {}
#
#     for letter in s:
#         if letter in chars:
#             chars[letter] += 1
#         else:
#             chars[letter] = 1
#
#     for letter in s:
#         if chars[letter] == 1:
#             return letter
#
#     return None


# print(unique("I Peel Ape Bananas"))


# returning all unique characters

def unique2(s):
    s = s.replace(" ", "").lower()
    chars = {}

    for letter in s:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1

    all_uniques = []

# sorts the dictionary by key value
# y = sorted(chars.items(), key=lambda x: x[1])

    for letter in s:
        if chars[letter] == 1:
            all_uniques.append(letter)

    return all_uniques


print(unique2("I Peel Ape Bananas"))
