def parabola_directrix(a, b, c):
    if a == 0:
        raise ValueError("'a' should not be equal to 0")
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("Discriminant is negative, parabola does not intersect x-axis")
    directrix = -b / (2*a)
    return directrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5,3,2), -198)

if __name__ == '__main__':
    unittest.main()