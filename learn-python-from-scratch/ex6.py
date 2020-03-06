#!/usr/bin/env python3

'''
You must implement the check_sum() function which takes in a list and returns True if the sum of two numbers in the list is zero. If no such pair exists, return False.

|10|-14|26|5|-3|13|-5|
(5,-5) => 0 => True
|10|-14|26|5|-3|
=> False

Sample Input #
[10, -14, 26, 5, -3, 13, -5]

Sample Output #
True
'''

def check_sum(num_list): # The argument is a list of integers
  for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
      if num_list[i] + num_list[j] == 0:
        return True
  return False

print("Opposites[]: "+str(check_sum([])))
print("Opposites[1,2]: "+str(check_sum([1,2])))
print("Opposites[-2,2]: "+str(check_sum([-2,2])))
