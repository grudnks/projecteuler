#!/usr/bin/env python3

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

def get_sum_of_primes_below(n):    
    prime_sum = 0
    i = 1
    while i < n:
        i += 1
        if isPrime(i):
            prime_sum += i
    return prime_sum

print(get_sum_of_primes_below(2000000))
# Answer: 142913828922