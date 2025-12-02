def triangle_area(r):
    if r < 0:
        return None
    else:
        return (r**2) / 2
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(2), 4)
        self.assertEqual(triangle_area(3), 9)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()