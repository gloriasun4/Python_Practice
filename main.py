### String Concatenation ###

youtuber = "Gloria"
# simple
print("Subscribe to " + youtuber)
# puts value of youtuber into curly braces
print("Subscribe to {}".format(youtuber))
#fstring
print(f"Subscribe to {youtuber}")

## madlibs ##
adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

#using fstring, \ means new line
madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)