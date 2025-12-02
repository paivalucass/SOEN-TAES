import cmath

def convert(number):
    try:
        polar = (abs(number), cmath.phase(number))
        return polar
    except TypeError:
        raise ValueError("Invalid input")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()