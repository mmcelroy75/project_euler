'''
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import numpy as np

def py_trip():
    triplet_list = []

    m = 11
    n = 10

    while True:

        a = (m**2)  - (n**2)
        b = (2 * m) * n
        c = (m**2) + (n**2)

        if ((a**2) + (b**2) == c**2):
            triplet_list = [a, b, c]
            if sum(triplet_list) == 1000:
                break
            else:
                m += 1
                n += 1
        
    return triplet_list, np.prod(triplet_list)

print(py_trip())
