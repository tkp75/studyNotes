#!/usr/bin/env python3

random_set = set({"Educative", 1408, 3.142, (True, False)})
print (random_set)

random_set.discard(1408)
print (random_set)

random_set.remove((True, False))
print (random_set)
