#!/usr/bin/env python3

'''
Sample Input:

G =      6.67 * 10^-11
MEarth = 6.0 * 10^24
mMoon =  7.34 * 10^22
r =      3.84 * 10^8

Sample Output:

FG =     1.99 * 10^20
'''


G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24) # Mass of Earth
m = 7.34 * (10 ** 22) # Mass of the moon
r = 3.84 * (10 ** 8)

grav_force = G*M*m/r**2

print(grav_force)
