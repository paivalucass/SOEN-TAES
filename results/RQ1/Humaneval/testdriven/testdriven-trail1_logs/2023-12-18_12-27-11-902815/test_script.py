def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        return "Input must be greater than 1"

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Suggestions:
# - The code is not well-documented. It would be helpful to add comments explaining the purpose of each section of the code. Additionally, it would be good to add input validation to ensure that the input is an integer.
# - There are no test cases provided for this function. It would be beneficial to create test cases to cover different scenarios, such as testing with prime and non-prime numbers, as well as edge cases like 0 and negative numbers.
# Original code:
# def largest_prime_factor(n: int):
#     if n < 2:
#         return "Input must be greater than 1"
#     
#     i = 2
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#     return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()