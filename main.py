### Unique Characters ###

"""
Given a string, are all characters unique?
returns a boolean
"""


# with python built-in structures

"""
def unique(s):
    s = s.replace(" ", "")
    return len(set(s)) == len(s)


print(unique("a b cde f"))
"""


def unique(s):
    s = s.replace(" ", "")
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True


print(unique("a bb cde f"))
