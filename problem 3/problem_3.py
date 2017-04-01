#!/usr/bin/env python3

def get_lpf(n):
    i = 2
    while i**2 < n:
        while n % i == 0:
            n = n/i
        i += 1
    return int(n) 

print(get_lpf(600851475143))
# Answer: 6857