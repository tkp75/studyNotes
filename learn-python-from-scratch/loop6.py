#!/usr/bin/env python3

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
result = ()
found = False # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            result = (n1, n2)
            found = True # Set found to True
            break # Break inner loop if a pair is found
    if found == True:
        break # Break outer loop if a pair is found

print (result)
