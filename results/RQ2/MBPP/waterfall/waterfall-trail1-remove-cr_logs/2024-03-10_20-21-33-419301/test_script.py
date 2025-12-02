def parabola_directrix(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "Error: Coefficients should be numeric"
    if a <= 0 or b <= 0 or c <= 0:
        return "Error: Coefficients cannot be negative"
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Error: Discriminant is negative, no real roots"
    
    directrix = (-b**2 + discriminant)/(4*a)
    return directrix

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()