#!/usr/bin/env python3

'''
As we saw earlier, the Fibonacci sequence is a series of numbers where every number is the sum of the two numbers before it. The first two numbers are 0 and 1:

0 1 1 2 3 5 8 13

You must write the fib() function which takes in a positive integer, n, and returns the n-th Fibonacci number. However, instead of using recursion, your function must use any of the loops.

Sample Input #
n = 7

Sample Output #
8
'''

def fib(n):
  if n < 1:
    return 0
  if n == 1:
    return 1
  val = [ 0, 1 ]
  for i in range(2,n):
    val.append(val[i-1]+val[i-2])
  return val[n-1]

print(fib(10))
