#!/usr/bin/env python3

def get_sm(n):
    num = 1
    for i in range(2, n+1):
        counter = 1
        while True:
            prod = counter * num
            if prod % i != 0:
                counter += 1
            else:
                num = prod
                break
    return num 

print(get_sm(20))
# Answer: 232792560