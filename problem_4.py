# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 ×99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys

size = sys.argv[1]

def biggest_palindrome(size):
    biggest = 0
    tuple = [0,0,'']
    top = a = b = int("9"*int(size))
    for i in range(a, 0, -1):
        for j in range (b, 0, -1):
            word = str(i * j)
            if word == ''.join(reversed(word)):
                if int(word) > biggest:
                    biggest = int(word)
                    triple = [i,j,word]
                    print(triple)
    return biggest
print(biggest_palindrome(size))
# print(thing)
#     word = str(a*b)
    # print(word)
    # length = len(word) - 1 
    # print(length)
    # for j in range(0,length//2):
        # print(word[j], word[length//2])
        # while word[j] == word[length - j]:
        # j =+ 1 
    
    

