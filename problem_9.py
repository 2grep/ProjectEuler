import math

def is_py_triple(a,b,c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

def find_triple_of_sum(n):
    triple = [0,0,0]
    winners = []
    for a in range(1,int(n//2)):
        for b in range(1,int(n//2)):
            for c in range(1,int(n//2)):
                if is_py_triple(a,b,c):
                    if a + b + c == n:
                        winners.append([a, b, c, a*b*c])
    return winners 