# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 0 to 20?

# import sys

# size = sys.argv[1]
from primeFactors import prime_factors
from collections import Counter

# scm = size
n = 10
def least_cm(n):
    values = {x: 0 for x in range(1,n+1)}
    for i in range(2,len(values)+1):
        counts = dict(Counter(prime_factors(i)))
        for j in range(0,len(counts)+1):
            print(counts[j]," ",values[j])
            if counts[j] > values[j]:
                values[j] = counts[j]
    return values




#     while any(v == 0 for v in required.values()):
#         scm =+ 1
#         if scm % i == 0:
#             required[i] = 1