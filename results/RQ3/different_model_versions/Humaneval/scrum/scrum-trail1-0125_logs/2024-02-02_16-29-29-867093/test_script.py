def is_prime(n):
    """
    Check if a number is prime.
    
    Parameters:
    n (int): The number to check
    
    Returns:
    bool: True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """
    Return x if n is prime, y otherwise.
    
    Parameters:
    n (int): The number to check
    x (any): The value to return if n is prime
    y (any): The value to return if n is not prime
    
    Returns:
    any: x if n is prime, y otherwise
    """
    if is_prime(n):
        return x
    else:
        return y
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(15, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()