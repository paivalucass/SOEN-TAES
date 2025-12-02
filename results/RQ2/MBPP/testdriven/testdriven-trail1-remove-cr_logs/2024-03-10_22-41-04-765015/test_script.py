import math

def parabola_directrix(a, b, c):
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("The discriminant cannot be negative.")
    directrix = -b / (2*a)
    return directrix
import unittest

class Test(unittest.TestCase):
    def test_parabola_directrix(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()