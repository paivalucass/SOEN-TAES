from math import gcd
def find_solution(a, b, n):
    '''Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.'''
    if gcd(a, b) == 0:
        return None
    x, y = 0, n // b
    while True:
        if (n - b * y) % a == 0:
            x = (n - b * y) // a
            break
        y -= 1
    return (x, y)

assert find_solution(2, 3, 7) == (2, 1)
import unittest

class Test(unittest.TestCase):
    def test_find_solution(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()