import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s*s == x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

is_fibonacci(5) # True