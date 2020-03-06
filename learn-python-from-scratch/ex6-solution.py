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

def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False

num_list = [10, -14, 26, 5, -3, 13, -5]
print (check_sum(num_list))
