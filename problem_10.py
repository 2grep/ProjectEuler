import math

def sieve_of_eratosthenes(n):
    """
    Generates a list of prime numbers up to 'n' using the Sieve of Eratosthenes.
    """
    # Create a boolean list "is_prime[0...n]" and initialize all entries as True.
    # A value in is_prime[i] will be False if i is not a prime, else True.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers.

    # The outer loop only needs to go up to the square root of n.
    for p in range(2, int(math.sqrt(n)) + 1):
        # If is_prime[p] is not changed, then it is a prime.
        if is_prime[p]:
            # Update all multiples of p as False, starting from p*p
            # (smaller multiples were already marked by smaller primes).
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Collect all the numbers that are marked True into a list of primes.
    prime_numbers = [p for p, prime_status in enumerate(is_prime) if prime_status]
    return prime_numbers

# Example usage:
limit = 30
primes_up_to_30 = sieve_of_eratosthenes(limit)
print(f"Prime numbers up to {limit}: {primes_up_to_30}")