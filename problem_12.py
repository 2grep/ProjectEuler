import math

def divisors(n):
    """Finds all divisors of a number n efficiently."""
    divisors = set()
    # Iterate from 1 up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            # Add the other half of the pair, unless it's the square root itself (to avoid duplicates)
            if i * i != n:
                divisors.add(n // i)
    return sorted(list(divisors))

def triangular_number(n):
    tri_num = 0
    for i in range(1,n+1):
        tri_num = tri_num + i
    return tri_num

def solution(m):
    tri_num = 1
    max_divisors = 1
    n = 1
    while max_divisors < m:
        tri_num = triangular_number(n)
        divs = len(divisors(tri_num))
        max_divisors = max(max_divisors, divs)
        n += 1
    return tri_num
