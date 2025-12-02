def parabola_directrix(a, b, c):
    if a == 0:
        raise ValueError("The value of 'a' cannot be zero for the calculation")

    directrix = (b**2 - 4*a*c) / (4*a)
    return round(directrix, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()