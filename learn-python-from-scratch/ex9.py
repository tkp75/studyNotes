#!/usr/bin/env python3

'''
Given a list of integers and a number k, find the kth maximum element in the list. The element will be stored in the kth_min variable.

test_list=40,35,82,14,22,66,53
k=2					k=6
result=66		result=22

Coding Challenge
Take some time to figure out the smartest way to solve this problem. All the list methods and other data structures are available for use. The list being used is called 'test_list`.

Write the code in terms of k. You do not need to worry about its value. Assign the answer to kth_min.
'''

test_list=[40,35,82,14,22,66,53]
k=2
print(k)
print(test_list)
test_list.sort(reverse=True)
print(test_list)
kth_min=test_list[k-1]
print(kth_min) 
