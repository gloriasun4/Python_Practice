### Dynamic Arrays ###

"""
1) Given two strings, check to see if they are anagrams. An anagram is when the two strings
can be written using the exact same letters.
For example:
"public relations" is an anagram of "crap built on lies"
"clint eastwood" is an anagram of "old west action"
Ignore space and capitalization.
"""


# def anagrams(s1, s2):
#     s1 = s1.replace(' ', '').lower()
#     s2 = s2.replace(' ', '').lower()
#
#     return sorted(s1) == sorted(s2)
#
#
# print(anagrams("god", "dog"))
# print(anagrams("public relations", "crap built on lies"))


# NOT an optimal solution because it uses python modules (sorted)

# with counts and dictionaries


def anagrams2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    # empty dictionary
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagrams2("god", "dog"))
print(anagrams2("public relations", "crap built on lies"))
