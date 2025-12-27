# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

def generate_collatz_sequence(n):
    if n <= 0:
        print("n must be a positive integer!")
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n//2
            sequence.append(n)
        else:
            n = 3 * n + 1
            sequence.append(n)
    return sequence

def longest_collatz_seq(n):
    max_length = 0
    max_length_i = 0
    for i in range(n,1,-1):
        length = len(generate_collatz_sequence(i))
        if max_length < length:
            max_length_i = i
            max_length = length
    return [max_length_i, max_length]

print(longest_collatz_seq(1000000))

cache = {1: 1} # Base case: the length from 1 to 1 is 1 step (or 0 if you exclude the final 1)

def collatz_length(n):
    if n not in cache:
        if n % 2 == 0:
            # If even, length is 1 + length of n/2
            cache[n] = 1 + collatz_length(n // 2) 
        else:
            # If odd, length is 1 + length of 3n + 1
            cache[n] = 1 + collatz_length(3 * n + 1)
    return cache[n]