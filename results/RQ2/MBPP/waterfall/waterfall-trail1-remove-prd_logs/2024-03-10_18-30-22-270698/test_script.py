import math

def find_solution(a, b, n):
    '''Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.'''
    if a == 0 and b == 0:
        return None
    if math.gcd(a, b) == 0:
        return (0, n//b) if n % b == 0 else None
    gcd = math.gcd(a, b)
    if n % gcd != 0:
        return None
    x = n // a
    y = (n - a * x) // b
    return (x, y) if (n - a * x) % b == 0 and y >= 0 else None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()