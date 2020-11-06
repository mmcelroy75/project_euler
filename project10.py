'''
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


import numpy as np
import time

def get_primes(number):
    prime_list = []

    is_prime = lambda number: all(number % i !=0 for i in range(2, int(number**.5)+1) )

    for i in range(2, number):
        if is_prime(i) == True:
            prime_list.append(i)
        else:
            pass
    
    total = np.sum(prime_list)
    
    return total

t1 = time.process_time()
print(get_primes(2_000_000))
t2 = time.process_time()
print(t2-t1)

#Answer is 142913828922