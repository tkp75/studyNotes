#!/usr/bin/env python3

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2:house+"!" for (n, house) in houses.items()}
print (houses)
print (new_houses)
