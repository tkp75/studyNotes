#!/usr/bin/env python3

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list: # Iterator goes traverses to the last index of the list
  if num > 10:
    count_greater += 1

print (count_greater)
