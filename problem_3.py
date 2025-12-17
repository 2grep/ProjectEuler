import sys

number = int(sys.argv[1])

def prime_factors(n):
    factors = []
    # Handle the factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd factors
    # Start checking from 3 and increment by 2 (to check only odd numbers)
    i = 3
    while i * i <= n:  # We only need to check up to the square root of n
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still greater than 2, it means n itself is a prime factor
    if n > 2:
        factors.append(n)
    return factors

print(prime_factors(number))