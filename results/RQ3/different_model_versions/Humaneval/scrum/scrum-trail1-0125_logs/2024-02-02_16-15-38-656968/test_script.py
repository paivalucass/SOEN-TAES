def triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError('Base and height must be positive values.')
    return 0.5 * base * height
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(5, 3), 7.5)

if __name__ == '__main__':
    unittest.main()