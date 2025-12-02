def triangle_area(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        return None
    else:
        return (radius ** 2) / 2
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(1), 0.5)
        self.assertEqual(triangle_area(2), 2)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()