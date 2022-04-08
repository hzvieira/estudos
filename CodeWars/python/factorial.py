'''
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of 
all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. 
By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 
throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).
'''
def factorial(n):
    fatorial = 1
    if n >= 0 and n <= 12:
        if n == 0:
            return fatorial
        for num in range(1, n + 1):
            fatorial = fatorial * num
    else:
        raise ValueError(-1)
    return fatorial