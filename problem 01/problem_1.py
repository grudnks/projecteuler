#!/usr/bin/env python3

def multiples(n,m):
    return sum(filter(lambda x: 
        x % n == 0 or x % m == 0,
        [x for x in range(1000)]))

print(multiples(3,5))
# Answer: 233168