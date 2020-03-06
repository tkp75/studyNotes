#!/usr/bin/env python3

def minimum (first, second):
    if (first < second):
        return first
    else:
        return second

num1 = 10
num2 = 20

result = minimum (num1, num2) # Storing the value returned by the function
print (result)
