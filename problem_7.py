# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    # Check for factors up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

# To find the 10,001st prime:
nth = 10001
prime_number = find_nth_prime(nth)
print(f"The {nth:,}th prime number is: {prime_number:,}")
