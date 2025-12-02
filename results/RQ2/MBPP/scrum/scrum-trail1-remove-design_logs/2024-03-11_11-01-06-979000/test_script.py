import math
import unittest

def triangle_area(r):
    if r <= 0:
        return None
    else:
        return (0.5 * r * r * math.sin(math.pi))
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(1), 0.5)
        self.assertEqual(triangle_area(2), 2.0)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()