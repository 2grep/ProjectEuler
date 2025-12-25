# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10) = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum

n = 100

def sum_of_squares(n):
    sumSquares = 0
    for i in range(1, n+1):
        sumSquares = sumSquares + i**2
    return sumSquares

def square_of_sum(n):
    squareSum = 0
    squareSum = (n * (n + 1)//2) **2
    return squareSum

print(square_of_sum(n) - sum_of_squares(n))
