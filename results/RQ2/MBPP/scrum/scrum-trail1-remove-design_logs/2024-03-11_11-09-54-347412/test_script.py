def area_tetrahedron(side):
    area = (3 ** 0.5) * (side ** 2)
    return area
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(area_tetrahedron(3), 15.588457268119894, places=10)

if __name__ == '__main__':
    unittest.main()