

# A number is a perfect square, or a square number, if it is the square of a positive integer.
# For example, 25
# is a square number because 52 =5 ×5 =25
# ; it is also an odd square.

# The first 5 square numbers are: 1,4,9,16,25
# , and the sum of the odd squares is 1 +9 +25 =35
# .

# Among the first 192 thousand square numbers, what is the sum of all the odd squares?

import sys

lim = sys.argv[1]
oddsum = 0
for n in range(0,lim):
    sq = n*n
    if sq % 2 != 0:
        oddsum = sq + oddsum
    n += 1
print(oddsum)

