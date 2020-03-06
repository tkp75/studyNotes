#!/usr/bin/env python3

num = 20

def multiply_by_10(n):
    n *= 10
    num = n # Changing the value inside the function
    print (num)
    return n

multiply_by_10(num)
print (num) # The original value remains unchanged
