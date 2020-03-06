#!/usr/bin/env python3

# When two strings have different lengths, the string which comes first in the dictionary is said to have the smaller value.
print ('a' < 'b') # 'a' has a smaller Unicode value

house = "Gryffindor"
house_copy = "Gryffindor"

print (house == house_copy)

new_house = "Slytherin"

print (house == new_house)

print (new_house <= house)

print (new_house >= house)
