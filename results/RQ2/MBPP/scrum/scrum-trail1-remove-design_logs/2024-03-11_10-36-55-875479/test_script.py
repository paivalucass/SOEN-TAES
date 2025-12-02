def parabola_directrix(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        return "Invalid input"

    if a == 0:
        return "Invalid input"

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"

    directrix = -b / (2*a)
    return directrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()