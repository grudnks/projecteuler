#!/usr/bin/env python3

def get_pythagorean_triplet(n):
    for c in range(n+1)[:-1]:
        for b in range(int(c/2), c)[:-1]:
            for a in range(int(b/2),b)[:-1]:
                if a + b + c == n:
                    if a**2 + b**2 == c**2:
                        return ([a,b,c], a*b*c)
    
print(get_pythagorean_triplet(1000))
# Answer: 31875000