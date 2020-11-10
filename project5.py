'''
Problem 5: 

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import math

divisors = range(1, 21)
numbers = []
n = 2520

while len(numbers) < 20:
    for i in divisors:
        if n % i == 0:
            numbers.append(n)
            n += 1

print(numbers)