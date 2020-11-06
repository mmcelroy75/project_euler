"""
Problem 6: 

The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(num1):
    sum = 0
    for i in range(1, num1+1):
        sum += i**2
    return sum

def square_of_sum(num1):
    sum = 0
    for i in range(num1, 0, -1):
        sum += i
    result = sum**2
    return result
    

first = sum_of_squares(100)
    
second = square_of_sum(100)

print(first)
print(second)
print(second - first)