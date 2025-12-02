def is_prime_number(n, prime_return_value, non_prime_return_value):
    """
    This function returns prime_return_value if the input n is a prime number,
    and non_prime_return_value if it is not.
    """
    if n < 2:
        return non_prime_return_value
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return non_prime_return_value
    return prime_return_value

def x_or_y(n, x, y):
    """
    A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if is_prime_number(n, x, y) == x:
        return x
    else:
        return y
import unittest

class Test(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()