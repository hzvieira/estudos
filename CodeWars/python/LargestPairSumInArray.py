# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def largest_pair_sum(numbers): 
    numerosOrdenados = sorted(numbers, reverse=True)
    return numerosOrdenados[0] + numerosOrdenados[1]

# Boas práticas
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])