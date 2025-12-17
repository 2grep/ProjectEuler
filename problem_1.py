# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3,5,6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

lim = int(sys.argv[1])
sum = 0
for n in range(0,lim):
    if n % 3 == 0 and n % 5 == 0:
        sum += n
        print(n,sum)
    elif n % 5 == 0:
        sum += n
        print(n,sum)
    elif n % 3 == 0:
        sum += n
        print(n,sum)
    else:
        print(',')
    n += 1
print(sum)
