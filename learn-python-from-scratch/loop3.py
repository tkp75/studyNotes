#!/usr/bin/env python3

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print (float_list)

for i in range(0, len(float_list)): # Iterator goes traverses to the last index of the list
  float_list[i] = float_list[i] * 2

print (float_list)
