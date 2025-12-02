def find(n, m):
    """
    Calculate the quotient of two numbers n and m, rounded down to the nearest integer
    Args:
    n (int): the first number
    m (int): the second number
    Returns:
    int: the rounded down quotient of n and m
    """
    if type(n) != int or type(m) != int:
        return "Error: Invalid input format"
    if m == 0:
        return "Error: Division by zero"
    return n // m
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()