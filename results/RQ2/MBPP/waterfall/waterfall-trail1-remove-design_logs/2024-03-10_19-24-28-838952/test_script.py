def area_tetrahedron(side):
    return (side ** 3) * ((2 ** 0.5) * ((3 ** 0.5) / 4)) / 12
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(area_tetrahedron(3), 15.588457268119894)

if __name__ == '__main__':
    unittest.main()