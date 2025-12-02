def parabola_directrix(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("Input coefficients must be numeric")
    
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        raise ValueError("The parabola does not intersect the x-axis, invalid input coefficients")
    
    directrix = -b / (2 * a)
    
    return directrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()